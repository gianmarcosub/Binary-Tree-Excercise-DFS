import keyword
import random
import re
import threading
import tkinter as tk
from tkinter import ttk

import ai_config
import stats_tracker


# Pool of algorithms the AI is asked to implement. The display name is shown
# on the answer buttons; the prompt phrase is what we ask Gemini to write.
ALGORITHMS = [
    ("Bubble Sort", "the bubble sort algorithm"),
    ("Selection Sort", "the selection sort algorithm"),
    ("Insertion Sort", "the insertion sort algorithm"),
    ("Merge Sort", "the merge sort algorithm"),
    ("Quick Sort", "the quicksort algorithm"),
    ("Heap Sort", "the heap sort algorithm"),
]


def _strip_code_fences(text):
    """Remove ```python ... ``` markdown fences if the model added them."""
    text = text.strip()
    fence = re.match(r"^```[a-zA-Z]*\n(.*)\n```$", text, re.DOTALL)
    if fence:
        return fence.group(1).strip()
    if text.startswith("```") and text.endswith("```"):
        return text.strip("`").strip()
    return text


# Identifiers/words that would let the player recognise the algorithm just by
# reading a name (function names, helper names, telltale variables).
GIVEAWAY_WORDS = {
    "bubble", "selection", "insertion", "merge", "mergesort", "quick",
    "quicksort", "qsort", "pivot", "partition", "heap", "heapsort", "heapify",
    "sift", "siftdown", "siftup", "bubblesort", "binary", "binsearch",
    "bisect", "linear", "sort", "sorting", "sorted", "search", "find",
    "dfs", "bfs", "depth", "breadth", "traverse", "traversal", "preorder",
    "inorder", "postorder", "fib", "fibonacci", "factorial", "fact",
    "gcd", "euclid", "dijkstra", "shortest", "graph", "adjacency", "adj",
    "neighbor", "neighbors", "neighbour", "neighbours", "visited", "frontier",
    "queue", "stack", "distance", "distances", "dist", "priority",
    # stdlib helpers whose names reveal the algorithm
    "heapq", "heappush", "heappop", "heapreplace", "heappushpop", "bisect",
    "insort", "deque", "popleft", "appendleft",
}

# Neutral replacement identifiers (valid Python names, no semantic hint).
_NEUTRAL_POOL = [
    "f", "g", "h", "p", "q", "r", "s", "t", "u", "v", "w",
    "aux", "tmp", "acc", "res", "cur", "nxt", "buf", "seq", "coll",
    "node", "item", "elem", "grp", "reg", "obj", "tot", "stp", "blk",
]


def _obfuscate(code):
    """Strip comments and rename revealing identifiers consistently.

    Every function definition name and every telltale word (e.g. ``pivot``,
    ``merge``, ``heapify``) is replaced by a neutral name. Replacement is
    consistent so the code stays internally coherent and readable.
    """
    # Drop full-line and trailing # comments (best effort, ignores # in strings).
    lines = []
    for line in code.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("#"):
            continue
        if "#" in line and '"' not in line and "'" not in line:
            line = line[: line.index("#")].rstrip()
        lines.append(line.rstrip())
    # Collapse runs of 3+ blank lines down to one.
    code = re.sub(r"\n{3,}", "\n\n", "\n".join(lines))

    # Names to rename: all defined functions + giveaway tokens present.
    all_tokens = set(re.findall(r"\b\w+\b", code))
    func_names = set(re.findall(r"\bdef\s+(\w+)", code))
    rename = func_names | {t for t in all_tokens if t.lower() in GIVEAWAY_WORDS}
    rename = {t for t in rename if not keyword.iskeyword(t)}
    # Identifiers we must NOT collide with: every token that stays unchanged.
    reserved = all_tokens - rename

    mapping = {}
    pool = iter(_NEUTRAL_POOL)

    def neutral():
        for name in pool:
            if name not in reserved and name not in mapping.values():
                return name
        i = 0
        while True:
            cand = f"v{i}"
            if cand not in reserved and cand not in mapping.values():
                return cand
            i += 1

    # Functions first (so they get the short f/g/h names), then other tokens.
    for tok in sorted(rename, key=lambda x: (x not in func_names, x)):
        mapping[tok] = neutral()

    for old, new in mapping.items():
        code = re.sub(rf"\b{re.escape(old)}\b", new, code)
    return code.strip()


class AIConfigDialog(tk.Toplevel):
    """Modal dialog to enter the Gemini API key and pick a model."""

    def __init__(self, parent, controller, on_saved=None):
        super().__init__(parent)
        self.controller = controller
        self.on_saved = on_saved
        self.title(controller.t("ai_config_title"))
        self.configure(bg="#f0f0f0")
        self.geometry("560x300")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()

        cfg = ai_config.load()

        tk.Label(
            self, text=controller.t("ai_config_title"),
            font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#222",
        ).pack(pady=(14, 10))

        body = tk.Frame(self, bg="#f0f0f0")
        body.pack(padx=20, fill=tk.X)

        tk.Label(
            body, text=controller.t("ai_config_key_label"),
            font=("Arial", 11, "bold"), bg="#f0f0f0",
        ).grid(row=0, column=0, sticky="w", pady=6)
        self.var_key = tk.StringVar(value=cfg["api_key"])
        self.entry_key = tk.Entry(
            body, textvariable=self.var_key, width=44, show="•",
            font=("Consolas", 10),
        )
        self.entry_key.grid(row=0, column=1, sticky="we", pady=6, padx=(8, 0))

        self.var_show = tk.BooleanVar(value=False)
        tk.Checkbutton(
            body, text=controller.t("ai_config_show_key"),
            variable=self.var_show, bg="#f0f0f0", command=self._toggle_key,
        ).grid(row=1, column=1, sticky="w")

        tk.Label(
            body, text=controller.t("ai_config_model_label"),
            font=("Arial", 11, "bold"), bg="#f0f0f0",
        ).grid(row=2, column=0, sticky="w", pady=6)
        self.var_model = tk.StringVar(value=cfg["model"])
        ttk.Combobox(
            body, textvariable=self.var_model, width=28, state="readonly",
            values=ai_config.MODELS,
        ).grid(row=2, column=1, sticky="w", pady=6, padx=(8, 0))

        body.columnconfigure(1, weight=1)

        tk.Label(
            self,
            text=controller.t("ai_config_key_hint", url=ai_config.API_KEY_URL),
            font=("Arial", 9, "italic"), bg="#f0f0f0", fg="#1565C0",
        ).pack(pady=(12, 0))

        btns = tk.Frame(self, bg="#f0f0f0")
        btns.pack(pady=18)
        tk.Button(
            btns, text=controller.t("ai_config_save"), command=self._save,
            bg="#2E7D32", fg="white", font=("Arial", 11, "bold"),
            padx=14, pady=5, cursor="hand2",
        ).pack(side=tk.LEFT, padx=6)
        tk.Button(
            btns, text=controller.t("ai_config_cancel"), command=self.destroy,
            bg="#757575", fg="white", font=("Arial", 11, "bold"),
            padx=14, pady=5, cursor="hand2",
        ).pack(side=tk.LEFT, padx=6)

    def _toggle_key(self):
        self.entry_key.config(show="" if self.var_show.get() else "•")

    def _save(self):
        ai_config.save(self.var_key.get(), self.var_model.get())
        from tkinter import messagebox
        messagebox.showinfo(
            self.controller.t("ai_config_title"),
            self.controller.t("ai_config_saved"),
        )
        if self.on_saved:
            self.on_saved()
        self.destroy()


class AIExerciseScreen(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root, bg="#f0f0f0")
        self.controller = controller
        self.current = None
        self.answered = False
        self.loading = False
        self.option_buttons = []
        self._build_ui()
        self._apply_language()
        self._refresh_state()

    def t(self, key, **fmt):
        return self.controller.t(key, **fmt)

    def _build_ui(self):
        top = tk.Frame(self, bg="#e0e0e0", pady=8, padx=10, relief=tk.RAISED, bd=2)
        top.pack(fill=tk.X, padx=10, pady=(10, 5))

        self.btn_back = tk.Button(
            top, command=self.controller.show_menu, bg="#757575", fg="white",
            font=("Arial", 10, "bold"), padx=8,
        )
        self.btn_back.pack(side=tk.LEFT, padx=(0, 12))

        self.lbl_lang = tk.Label(top, bg="#e0e0e0", font=("Arial", 10, "bold"))
        self.lbl_lang.pack(side=tk.LEFT)
        self.var_lang = tk.StringVar(
            value=self.controller.lang_name(self.controller.lang)
        )
        self.cb_lang = ttk.Combobox(
            top, textvariable=self.var_lang, width=12, state="readonly",
            values=self.controller.lang_values(),
        )
        self.cb_lang.pack(side=tk.LEFT, padx=(4, 15))
        self.cb_lang.bind("<<ComboboxSelected>>", self._on_language_change)

        self.lbl_title = tk.Label(
            top, bg="#e0e0e0", font=("Arial", 13, "bold"), fg="#333"
        )
        self.lbl_title.pack(side=tk.LEFT, padx=20)

        self.btn_config = tk.Button(
            top, command=self._open_config, bg="#455A64", fg="white",
            font=("Arial", 10, "bold"), padx=8,
        )
        self.btn_config.pack(side=tk.RIGHT, padx=5)

        self.btn_new = tk.Button(
            top, command=self.nuovo_esercizio, bg="#009688", fg="white",
            font=("Arial", 10, "bold"), padx=8,
        )
        self.btn_new.pack(side=tk.RIGHT, padx=5)

        center = tk.Frame(self, bg="#f0f0f0")
        center.pack(expand=True, fill=tk.BOTH, padx=10, pady=8)

        self.lbl_question = tk.Label(
            center, text="", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#333",
            wraplength=1000, justify="center",
        )
        self.lbl_question.pack(pady=(4, 4))

        self.lbl_model = tk.Label(
            center, text="", font=("Arial", 9, "italic"), bg="#f0f0f0", fg="#888",
        )
        self.lbl_model.pack(pady=(0, 6))

        code_frame = tk.Frame(center, bd=2, relief=tk.SUNKEN, bg="#1e1e1e")
        code_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=4)

        self.text_code = tk.Text(
            code_frame, font=("Consolas", 13), bg="#1e1e1e", fg="#dcdcdc",
            insertbackground="#dcdcdc", padx=14, pady=10, bd=0, wrap="none",
            height=14,
        )
        self.text_code.pack(expand=True, fill=tk.BOTH)
        self.text_code.configure(state=tk.DISABLED)

        bottom = tk.Frame(self, bg="#f0f0f0", pady=8)
        bottom.pack(fill=tk.X, padx=10, side=tk.BOTTOM)

        self.lbl_pick = tk.Label(
            bottom, text="", font=("Arial", 11, "italic"), bg="#f0f0f0", fg="#555",
        )
        self.lbl_pick.pack(pady=(0, 6))

        self.options_frame = tk.Frame(bottom, bg="#f0f0f0")
        self.options_frame.pack()

        self.lbl_feedback = tk.Label(
            bottom, text="", font=("Arial", 11, "bold"), bg="#f0f0f0",
            wraplength=1000, justify="center",
        )
        self.lbl_feedback.pack(pady=8)

    def _apply_language(self):
        self.btn_back.config(text=self.t("back"))
        self.lbl_lang.config(text=self.t("language"))
        self.lbl_title.config(text=self.t("ai_title"))
        self.btn_new.config(text=self.t("ai_generate"))
        self.btn_config.config(text=self.t("ai_open_config"))
        self.lbl_pick.config(text=self.t("ai_pick"))
        self.var_lang.set(self.controller.lang_name(self.controller.lang))

    def _on_language_change(self, _e=None):
        chosen = self.var_lang.get()
        self.controller.set_language_by_name(chosen)
        self._apply_language()
        self._refresh_state()

    def _open_config(self):
        AIConfigDialog(self, self.controller, on_saved=self._refresh_state)

    def _set_code(self, text):
        self.text_code.configure(state=tk.NORMAL)
        self.text_code.delete("1.0", tk.END)
        self.text_code.insert("1.0", text)
        self.text_code.configure(state=tk.DISABLED)

    def _clear_options(self):
        for b in self.option_buttons:
            b.destroy()
        self.option_buttons = []

    def _refresh_state(self):
        """Show either the 'configure AI' prompt or the question prompt."""
        self._clear_options()
        self.lbl_feedback.config(text="")
        if not ai_config.is_configured():
            self.lbl_question.config(text=self.t("ai_not_configured"))
            self.lbl_model.config(text="")
            self._set_code("")
            self.btn_new.config(state=tk.DISABLED)
        else:
            self.lbl_question.config(text=self.t("ai_question"))
            cfg = ai_config.load()
            self.lbl_model.config(text=self.t("ai_model_label", model=cfg["model"]))
            self.btn_new.config(state=tk.NORMAL)
            if self.current is None:
                self._set_code("")

    def nuovo_esercizio(self):
        if self.loading or not ai_config.is_configured():
            return
        self.loading = True
        self.answered = False
        self.current = None
        self._clear_options()
        self.lbl_feedback.config(text="")
        self.btn_new.config(state=tk.DISABLED)
        self._set_code(self.t("ai_generating"))

        display, desc = random.choice(ALGORITHMS)
        prompt = (
            "Write a single, idiomatic Python implementation of "
            f"{desc}. Use ONLY generic, neutral identifiers (e.g. f, g, a, "
            "b, i, j, tmp): the function name and every variable must NOT "
            "reveal which algorithm it is. Do not use names like sort, "
            "merge, pivot, heap, bfs, dfs, fib, gcd, etc. Do not call "
            "built-in sorted() or library helpers that name the algorithm. "
            "Output ONLY the raw Python code: no comments, no docstrings, "
            "no explanations, no markdown code fences, no example usage."
        )

        def worker():
            try:
                code = ai_config.generate_code(prompt)
                code = _obfuscate(_strip_code_fences(code))
                self.after(0, lambda: self._on_code_ready(display, code))
            except Exception as e:  # noqa: BLE001
                msg = str(e)
                self.after(0, lambda: self._on_error(msg))

        threading.Thread(target=worker, daemon=True).start()

    def _on_error(self, msg):
        self.loading = False
        self.btn_new.config(state=tk.NORMAL)
        self._set_code("")
        self.lbl_feedback.config(text=self.t("ai_error", err=msg), fg="#F44336")

    def _on_code_ready(self, correct_display, code):
        self.loading = False
        self.btn_new.config(state=tk.NORMAL)
        if not code:
            self._on_error(self.t("ai_error", err="empty response"))
            return

        self._set_code(code)
        self.current = {"answer": correct_display}

        others = [d for d, _ in ALGORITHMS if d != correct_display]
        distractors = random.sample(others, k=min(3, len(others)))
        options = distractors + [correct_display]
        random.shuffle(options)

        self._clear_options()
        for opt in options:
            b = tk.Button(
                self.options_frame, text=opt,
                command=lambda o=opt: self.verifica(o),
                bg="#2196F3", fg="white", font=("Arial", 11, "bold"),
                padx=8, pady=4,
            )
            b.pack(side=tk.LEFT, padx=4)
            self.option_buttons.append(b)

    def verifica(self, choice):
        if self.answered or self.current is None:
            return
        self.answered = True
        correct = self.current["answer"]
        is_right = choice == correct
        stats_tracker.record("ai", is_right)
        for b in self.option_buttons:
            b.config(state=tk.DISABLED)
            if b.cget("text") == correct:
                b.config(bg="#4CAF50")
            elif b.cget("text") == choice and not is_right:
                b.config(bg="#F44336")
            else:
                b.config(bg="#9E9E9E")

        if is_right:
            self.lbl_feedback.config(
                text=self.t("ai_correct", ans=correct), fg="#4CAF50"
            )
        else:
            self.lbl_feedback.config(
                text=self.t("ai_wrong", ans=correct), fg="#F44336"
            )

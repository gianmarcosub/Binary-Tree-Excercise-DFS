import tkinter as tk
from tkinter import ttk
from collections import deque
import random


BFS_TRANSLATIONS = {
    "it": {
        "menu_bfs": "Visita BFS\nLevel-order (livello per livello)",
        "bfs_levelorder": "LEVEL-ORDER (BFS)",
        "bfs_levelorder_hint": "Livello per livello, da sinistra a destra",
    },
    "en": {
        "menu_bfs": "BFS Traversal\nLevel-order (level by level)",
        "bfs_levelorder": "LEVEL-ORDER (BFS)",
        "bfs_levelorder_hint": "Level by level, left to right",
    },
    "es": {
        "menu_bfs": "Recorrido BFS\nLevel-order (nivel por nivel)",
        "bfs_levelorder": "LEVEL-ORDER (BFS)",
        "bfs_levelorder_hint": "Nivel por nivel, de izquierda a derecha",
    },
    "fr": {
        "menu_bfs": "Parcours BFS\nLevel-order (niveau par niveau)",
        "bfs_levelorder": "LEVEL-ORDER (BFS)",
        "bfs_levelorder_hint": "Niveau par niveau, de gauche à droite",
    },
    "de": {
        "menu_bfs": "BFS-Traversierung\nLevel-Order (Ebene für Ebene)",
        "bfs_levelorder": "LEVEL-ORDER (BFS)",
        "bfs_levelorder_hint": "Ebene für Ebene, von links nach rechts",
    },
    "pt": {
        "menu_bfs": "Percurso BFS\nLevel-order (nível por nível)",
        "bfs_levelorder": "LEVEL-ORDER (BFS)",
        "bfs_levelorder_hint": "Nível por nível, da esquerda para a direita",
    },
}


class _Nodo:
    __slots__ = ("valore", "sinistra", "destra", "x", "y")

    def __init__(self, valore):
        self.valore = valore
        self.sinistra = None
        self.destra = None
        self.x = 0.0
        self.y = 0.0


class BFSScreen(tk.Frame):
    H_SPACING = 45
    V_SPACING = 80
    MARGIN = 40
    RAGGIO = 18

    def __init__(self, root, controller):
        super().__init__(root, bg="#f0f0f0")
        self.controller = controller
        self.zoom_level = 1.0
        self.albero = None
        self.sequenza_corretta = []
        self._build_ui()
        self._apply_language()
        self.genera_nuovo_quiz()

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
        lang_pairs = self.controller.language_options()
        current_name = next(name for code, name in lang_pairs if code == self.controller.lang)
        self.var_lang = tk.StringVar(value=current_name)
        self.cb_lang = ttk.Combobox(
            top, textvariable=self.var_lang, width=12, state="readonly",
            values=[name for _c, name in lang_pairs],
        )
        self.cb_lang.pack(side=tk.LEFT, padx=(4, 15))
        self.cb_lang.bind("<<ComboboxSelected>>", self._on_language_change)

        self.lbl_depth = tk.Label(top, bg="#e0e0e0", font=("Arial", 10, "bold"))
        self.lbl_depth.pack(side=tk.LEFT)
        self.var_profondita = tk.IntVar(value=3)
        tk.Spinbox(
            top, from_=2, to=8, textvariable=self.var_profondita, width=4, font=("Arial", 10),
        ).pack(side=tk.LEFT, padx=(4, 15))

        self.var_bilanciato = tk.BooleanVar(value=False)
        self.chk_bilanciato = tk.Checkbutton(
            top, variable=self.var_bilanciato, bg="#e0e0e0", font=("Arial", 10),
        )
        self.chk_bilanciato.pack(side=tk.LEFT, padx=5)

        self.var_hint = tk.BooleanVar(value=True)
        self.chk_hint = tk.Checkbutton(
            top, variable=self.var_hint, bg="#e0e0e0", font=("Arial", 10),
            command=self._update_question_label,
        )
        self.chk_hint.pack(side=tk.LEFT, padx=5)

        self.btn_genera = tk.Button(
            top, command=self.genera_nuovo_quiz, bg="#00BCD4", fg="white",
            font=("Arial", 10, "bold"), padx=8,
        )
        self.btn_genera.pack(side=tk.RIGHT, padx=5)

        zoom_bar = tk.Frame(self, bg="#f0f0f0")
        zoom_bar.pack(fill=tk.X, padx=10)
        self.btn_zoom_out = tk.Button(zoom_bar, command=lambda: self._zoom(0.8), width=4)
        self.btn_zoom_in = tk.Button(zoom_bar, command=lambda: self._zoom(1.25), width=4)
        self.btn_zoom_reset = tk.Button(zoom_bar, command=self._zoom_reset, width=5)
        self.btn_fit = tk.Button(zoom_bar, command=self._fit_to_view, width=8)
        self.btn_zoom_out.pack(side=tk.LEFT, padx=2)
        self.btn_zoom_in.pack(side=tk.LEFT, padx=2)
        self.btn_zoom_reset.pack(side=tk.LEFT, padx=2)
        self.btn_fit.pack(side=tk.LEFT, padx=2)
        self.lbl_nodes = tk.Label(zoom_bar, bg="#f0f0f0", font=("Arial", 10, "italic"), fg="#555")
        self.lbl_nodes.pack(side=tk.RIGHT, padx=8)

        canvas_frame = tk.Frame(self, bd=2, relief=tk.SUNKEN)
        canvas_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)

        self.canvas = tk.Canvas(canvas_frame, bg="white", highlightthickness=0)
        hbar = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        vbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

        vbar.pack(side=tk.RIGHT, fill=tk.Y)
        hbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind("<Control-MouseWheel>", self._on_ctrl_wheel)
        self.canvas.bind("<Button-4>", lambda e: self._on_mousewheel_linux(e, 1))
        self.canvas.bind("<Button-5>", lambda e: self._on_mousewheel_linux(e, -1))
        self.canvas.bind("<ButtonPress-1>", lambda e: self.canvas.scan_mark(e.x, e.y))
        self.canvas.bind("<B1-Motion>", lambda e: self.canvas.scan_dragto(e.x, e.y, gain=1))

        bottom = tk.Frame(self, bg="#f0f0f0", pady=8)
        bottom.pack(fill=tk.X, padx=10, side=tk.BOTTOM)

        self.lbl_domanda = tk.Label(
            bottom, text="", font=("Arial", 13, "bold"), bg="#f0f0f0", fg="#333",
            wraplength=950, justify="center",
        )
        self.lbl_domanda.pack(pady=(0, 8))

        row = tk.Frame(bottom, bg="#f0f0f0")
        row.pack()
        self.lbl_seq = tk.Label(row, font=("Arial", 11), bg="#f0f0f0")
        self.lbl_seq.pack(side=tk.LEFT, padx=5)
        self.entry_risposta = tk.Entry(row, width=40, font=("Arial", 13), justify="center")
        self.entry_risposta.pack(side=tk.LEFT, padx=5)
        self.entry_risposta.bind("<Return>", lambda _e: self.verifica_risposta())
        self.btn_verifica = tk.Button(
            row, command=self.verifica_risposta, bg="#2196F3", fg="white",
            font=("Arial", 11, "bold"), padx=10,
        )
        self.btn_verifica.pack(side=tk.LEFT, padx=5)

        self.lbl_feedback = tk.Label(
            bottom, text="", font=("Arial", 11, "bold"), bg="#f0f0f0", justify="center",
        )
        self.lbl_feedback.pack(pady=8)

    def _apply_language(self):
        self.btn_back.config(text=self.t("back"))
        self.lbl_lang.config(text=self.t("language"))
        self.lbl_depth.config(text=self.t("depth"))
        self.chk_bilanciato.config(text=self.t("balanced"))
        self.chk_hint.config(text=self.t("show_hint"))
        self.btn_genera.config(text=self.t("generate"))
        self.btn_zoom_in.config(text=self.t("zoom_in"))
        self.btn_zoom_out.config(text=self.t("zoom_out"))
        self.btn_zoom_reset.config(text=self.t("zoom_reset"))
        self.btn_fit.config(text=self.t("fit"))
        self.lbl_seq.config(text=self.t("your_sequence"))
        self.btn_verifica.config(text=self.t("verify"))

        lang_pairs = self.controller.language_options()
        self.cb_lang["values"] = [name for _c, name in lang_pairs]
        current_name = next(name for code, name in lang_pairs if code == self.controller.lang)
        self.var_lang.set(current_name)

        self._update_question_label()
        self._update_node_count()

    def _on_language_change(self, _e=None):
        chosen = self.var_lang.get()
        for code, name in self.controller.language_options():
            if name == chosen:
                self.controller.set_language(code)
                break
        self._apply_language()

    def genera_albero(self, usati=None, profondita=0):
        if usati is None:
            usati = set()
        max_prof = self.var_profondita.get() - 1
        bilanciato = self.var_bilanciato.get()

        if profondita > max_prof:
            return None
        if not bilanciato and profondita > 0 and random.random() < 0.35:
            return None

        disponibili = [v for v in range(1, 100) if v not in usati]
        if not disponibili:
            return None
        valore = random.choice(disponibili)
        usati.add(valore)

        nodo = _Nodo(valore)
        nodo.sinistra = self.genera_albero(usati, profondita + 1)
        nodo.destra = self.genera_albero(usati, profondita + 1)
        return nodo

    def _layout(self, root):
        counter = [0]
        max_depth = [0]

        def walk(node, depth):
            if not node:
                return
            walk(node.sinistra, depth + 1)
            node.x = self.MARGIN + counter[0] * self.H_SPACING
            node.y = self.MARGIN + depth * self.V_SPACING
            counter[0] += 1
            if depth > max_depth[0]:
                max_depth[0] = depth
            walk(node.destra, depth + 1)

        walk(root, 0)
        n = max(counter[0], 1)
        width = 2 * self.MARGIN + (n - 1) * self.H_SPACING + 2 * self.RAGGIO
        height = 2 * self.MARGIN + max_depth[0] * self.V_SPACING + 2 * self.RAGGIO
        return width, height, counter[0]

    def _disegna(self, nodo):
        if not nodo:
            return
        if nodo.sinistra:
            self.canvas.create_line(
                nodo.x, nodo.y, nodo.sinistra.x, nodo.sinistra.y, width=2, fill="#555",
            )
            self._disegna(nodo.sinistra)
        if nodo.destra:
            self.canvas.create_line(
                nodo.x, nodo.y, nodo.destra.x, nodo.destra.y, width=2, fill="#555",
            )
            self._disegna(nodo.destra)
        r = self.RAGGIO
        self.canvas.create_oval(
            nodo.x - r, nodo.y - r, nodo.x + r, nodo.y + r,
            fill="#E0F7FA", outline="#00838F", width=2,
        )
        self.canvas.create_text(
            nodo.x, nodo.y, text=str(nodo.valore),
            font=("Arial", 11, "bold"), fill="#006064",
        )

    def _count_nodes(self, nodo):
        if not nodo:
            return 0
        return 1 + self._count_nodes(nodo.sinistra) + self._count_nodes(nodo.destra)

    def level_order(self, root):
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            node = q.popleft()
            result.append(node.valore)
            if node.sinistra:
                q.append(node.sinistra)
            if node.destra:
                q.append(node.destra)
        return result

    def genera_nuovo_quiz(self):
        self.canvas.delete("all")
        self.entry_risposta.delete(0, tk.END)
        self.lbl_feedback.config(text="")
        self.zoom_level = 1.0

        for _ in range(20):
            self.albero = self.genera_albero()
            if self.albero and self._count_nodes(self.albero) >= 3:
                break
        else:
            valori = random.sample(range(1, 100), 3)
            self.albero = _Nodo(valori[0])
            self.albero.sinistra = _Nodo(valori[1])
            self.albero.destra = _Nodo(valori[2])

        width, height, _ = self._layout(self.albero)
        self._disegna(self.albero)
        self.canvas.configure(scrollregion=(0, 0, width, height))
        self._update_node_count()

        self.sequenza_corretta = self.level_order(self.albero)
        self._update_question_label()
        self.entry_risposta.focus()
        self.after(50, self._fit_to_view)

    def _update_question_label(self):
        name = self.t("bfs_levelorder")
        if self.var_hint.get():
            hint = self.t("bfs_levelorder_hint")
            text = self.t("mission_hint", name=name, hint=hint)
        else:
            text = self.t("mission_plain", name=name)
        self.lbl_domanda.config(text=text)

    def _update_node_count(self):
        n = self._count_nodes(self.albero) if self.albero else 0
        self.lbl_nodes.config(text=self.t("nodes", n=n))

    def verifica_risposta(self):
        testo = self.entry_risposta.get().strip()
        if not testo:
            self.lbl_feedback.config(text=self.t("empty"), fg="#FF9800")
            return
        try:
            sequenza_utente = [int(x) for x in testo.replace(",", " ").split()]
        except ValueError:
            self.lbl_feedback.config(text=self.t("format_error"), fg="#FF9800")
            return
        if sequenza_utente == self.sequenza_corretta:
            self.lbl_feedback.config(text=self.t("correct"), fg="#4CAF50")
        else:
            self.lbl_feedback.config(
                text=self.t("wrong", user=sequenza_utente, correct=self.sequenza_corretta),
                fg="#F44336",
            )

    def _zoom(self, factor):
        new_level = self.zoom_level * factor
        if new_level < 0.1 or new_level > 5:
            return
        self.zoom_level = new_level
        self.canvas.scale("all", 0, 0, factor, factor)
        bbox = self.canvas.bbox("all")
        if bbox:
            self.canvas.configure(scrollregion=bbox)

    def _zoom_reset(self):
        if self.zoom_level == 0:
            return
        factor = 1.0 / self.zoom_level
        self._zoom(factor)

    def _fit_to_view(self):
        bbox = self.canvas.bbox("all")
        if not bbox:
            return
        x1, y1, x2, y2 = bbox
        content_w = max(x2 - x1, 1)
        content_h = max(y2 - y1, 1)
        view_w = max(self.canvas.winfo_width() - 20, 1)
        view_h = max(self.canvas.winfo_height() - 20, 1)
        factor = min(view_w / content_w, view_h / content_h)
        if factor <= 0:
            return
        self._zoom(factor)
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 if event.delta > 0 else 1, "units")

    def _on_ctrl_wheel(self, event):
        self._zoom(1.1 if event.delta > 0 else 0.9)

    def _on_mousewheel_linux(self, _event, direction):
        self.canvas.yview_scroll(-direction, "units")

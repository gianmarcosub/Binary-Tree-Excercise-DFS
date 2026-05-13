import tkinter as tk
from tkinter import ttk
import random

from sorting_table_exercise import (
    SORT_TABLE_DATA, BEST_OPTIONS, AVG_OPTIONS, WORST_OPTIONS, MEMORY_OPTIONS,
    values_match,
)


SORT_TABLE_ROW_TRANSLATIONS = {
    "it": {
        "sort_row_title": "Riga di Tabella Muta",
        "sort_row_intro": "Compila tutte le proprietà del seguente algoritmo:",
        "sort_row_new": "🔄 Nuovo Algoritmo",
    },
    "en": {
        "sort_row_title": "Blank Table Row",
        "sort_row_intro": "Fill in all properties of the following algorithm:",
        "sort_row_new": "🔄 New Algorithm",
    },
    "es": {
        "sort_row_title": "Fila de Tabla Muda",
        "sort_row_intro": "Rellena todas las propiedades del siguiente algoritmo:",
        "sort_row_new": "🔄 Nuevo Algoritmo",
    },
    "fr": {
        "sort_row_title": "Ligne du Tableau Muet",
        "sort_row_intro": "Remplis toutes les propriétés de l'algorithme suivant:",
        "sort_row_new": "🔄 Nouvel Algorithme",
    },
    "de": {
        "sort_row_title": "Zeile der leeren Tabelle",
        "sort_row_intro": "Fülle alle Eigenschaften des folgenden Algorithmus aus:",
        "sort_row_new": "🔄 Neuer Algorithmus",
    },
    "pt": {
        "sort_row_title": "Linha da Tabela em Branco",
        "sort_row_intro": "Preencha todas as propriedades do seguinte algoritmo:",
        "sort_row_new": "🔄 Novo Algoritmo",
    },
}


# (field_key, label_translation_key, options, kind, combobox_width)
FIELDS_SPEC = [
    ("in_place", "sort_table_col_inplace", None,           "yesno",   8),
    ("stable",   "sort_table_col_stable",  None,           "yesno",   8),
    ("best",     "sort_table_col_best",    BEST_OPTIONS,   "value",  16),
    ("avg",      "sort_table_col_avg",     AVG_OPTIONS,    "value",  16),
    ("worst",    "sort_table_col_worst",   WORST_OPTIONS,  "value",  16),
    ("memory",   "sort_table_col_memory",  MEMORY_OPTIONS, "value",  14),
]


class SortTableRowScreen(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root, bg="#f0f0f0")
        self.controller = controller
        self.current_idx = None
        self.cells = {}
        self.field_labels = []
        self.answered = False
        self._build_ui()
        self._apply_language()
        self.nuovo_esercizio()

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

        self.lbl_title = tk.Label(top, bg="#e0e0e0", font=("Arial", 13, "bold"), fg="#333")
        self.lbl_title.pack(side=tk.LEFT, padx=20)

        self.btn_new = tk.Button(
            top, command=self.nuovo_esercizio, bg="#607D8B", fg="white",
            font=("Arial", 10, "bold"), padx=8,
        )
        self.btn_new.pack(side=tk.RIGHT, padx=5)

        self.lbl_algo_name = tk.Label(
            self, bg="#f0f0f0", font=("Arial", 24, "bold italic"), fg="#333",
        )
        self.lbl_algo_name.pack(pady=(24, 4))

        self.lbl_intro = tk.Label(
            self, text="", bg="#f0f0f0", font=("Arial", 11), fg="#333",
            wraplength=1000, justify="center",
        )
        self.lbl_intro.pack(pady=(0, 16))

        form = tk.Frame(self, bg="#f0f0f0")
        form.pack(pady=8)

        for row_idx, (field_key, label_key, opts, kind, width) in enumerate(FIELDS_SPEC):
            lbl = tk.Label(
                form, bg="#f0f0f0", font=("Arial", 11, "bold"), anchor="e",
            )
            lbl.grid(row=row_idx, column=0, sticky="e", padx=(0, 12), pady=6)
            self.field_labels.append((lbl, label_key))

            var = tk.StringVar()
            cb = ttk.Combobox(form, textvariable=var, state="readonly", width=width)
            cb.grid(row=row_idx, column=1, sticky="w", pady=6)

            status = tk.Label(
                form, bg="#f0f0f0", font=("Arial", 10, "bold"), anchor="w",
            )
            status.grid(row=row_idx, column=2, sticky="w", padx=(12, 0), pady=6)

            self.cells[field_key] = {
                "var": var, "combobox": cb, "status": status,
                "kind": kind, "options": opts, "label_key": label_key,
            }

        action_frame = tk.Frame(self, bg="#f0f0f0")
        action_frame.pack(pady=14)

        self.btn_verify = tk.Button(
            action_frame, command=self.verifica, bg="#2196F3", fg="white",
            font=("Arial", 11, "bold"), padx=18, pady=4,
        )
        self.btn_verify.pack(side=tk.LEFT, padx=8)

        bottom = tk.Frame(self, bg="#f0f0f0", pady=8)
        bottom.pack(fill=tk.X, padx=10, side=tk.BOTTOM)

        self.lbl_feedback = tk.Label(
            bottom, text="", font=("Arial", 11, "bold"), bg="#f0f0f0",
            wraplength=1000, justify="center",
        )
        self.lbl_feedback.pack(pady=(8, 4))

        self.errors_frame = tk.Frame(bottom, bg="#f0f0f0")

        self.text_errors = tk.Text(
            self.errors_frame, height=5, font=("Consolas", 10),
            bg="#fafafa", fg="#333", wrap=tk.WORD, bd=1, relief=tk.SOLID,
            padx=8, pady=6,
        )
        err_sb = tk.Scrollbar(
            self.errors_frame, orient=tk.VERTICAL, command=self.text_errors.yview,
        )
        err_sb.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_errors.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.text_errors.configure(yscrollcommand=err_sb.set, state=tk.DISABLED)
        self.text_errors.tag_configure("wrong", foreground="#C62828")
        self.text_errors.tag_configure("empty", foreground="#FB8C00")

    def _apply_language(self):
        self.btn_back.config(text=self.t("back"))
        self.lbl_lang.config(text=self.t("language"))
        self.lbl_title.config(text=self.t("sort_row_title"))
        self.btn_new.config(text=self.t("sort_row_new"))
        self.lbl_intro.config(text=self.t("sort_row_intro"))
        self.btn_verify.config(text=self.t("sort_table_verify"))

        lang_pairs = self.controller.language_options()
        self.cb_lang["values"] = [name for _c, name in lang_pairs]
        current_name = next(name for code, name in lang_pairs if code == self.controller.lang)
        self.var_lang.set(current_name)

        for lbl, key in self.field_labels:
            lbl.config(text=self.t(key) + ":")

        placeholder = self.t("sort_table_pick")
        yes_str = self.t("sort_yes")
        no_str = self.t("sort_no")
        for cell in self.cells.values():
            if cell["kind"] == "yesno":
                cell["combobox"]["values"] = [placeholder, yes_str, no_str]
            else:
                cell["combobox"]["values"] = [placeholder] + cell["options"]
            cur = cell["var"].get()
            if cur not in cell["combobox"]["values"]:
                cell["var"].set(placeholder)
                cell["status"].config(text="")

    def _on_language_change(self, _e=None):
        chosen = self.var_lang.get()
        for code, name in self.controller.language_options():
            if name == chosen:
                self.controller.set_language(code)
                break
        self._apply_language()
        self.answered = False
        self.btn_verify.config(state=tk.NORMAL)
        for cell in self.cells.values():
            cell["combobox"].config(state="readonly")
        self.lbl_feedback.config(text="")
        self._clear_errors()

    def _clear_errors(self):
        self.errors_frame.pack_forget()
        self.text_errors.configure(state=tk.NORMAL)
        self.text_errors.delete("1.0", tk.END)
        self.text_errors.configure(state=tk.DISABLED)

    def nuovo_esercizio(self):
        choices = list(range(len(SORT_TABLE_DATA)))
        if self.current_idx is not None and len(choices) > 1:
            choices = [c for c in choices if c != self.current_idx]
        self.current_idx = random.choice(choices)

        self.lbl_algo_name.config(text=SORT_TABLE_DATA[self.current_idx][0])

        self.answered = False
        self.btn_verify.config(state=tk.NORMAL)
        self.lbl_feedback.config(text="")

        placeholder = self.t("sort_table_pick")
        for cell in self.cells.values():
            cell["var"].set(placeholder)
            cell["status"].config(text="")
            cell["combobox"].config(state="readonly")

        self._clear_errors()

    def verifica(self):
        if self.answered or self.current_idx is None:
            return

        placeholder = self.t("sort_table_pick")
        yes_str = self.t("sort_yes")
        no_str = self.t("sort_no")
        col_index = {"best": 1, "avg": 2, "worst": 3, "memory": 4, "stable": 5, "in_place": 6}

        algo_data = SORT_TABLE_DATA[self.current_idx]
        algo_name = algo_data[0]

        n_correct = n_wrong = n_empty = 0
        n_total = len(self.cells)
        error_lines = []

        for field_key, label_key, _opts, _kind, _w in FIELDS_SPEC:
            cell = self.cells[field_key]
            user_val = cell["var"].get()
            raw_expected = algo_data[col_index[field_key]]
            if cell["kind"] == "yesno":
                expected = yes_str if raw_expected else no_str
            else:
                expected = raw_expected
            col_label = self.t(label_key)

            if user_val == placeholder or user_val == "":
                cell["status"].config(text="—", fg="#9E9E9E")
                n_empty += 1
                error_lines.append((
                    self.t("sort_table_err_empty",
                           algo=algo_name, col=col_label, ans=expected),
                    "empty",
                ))
            elif values_match(user_val, expected, cell["kind"]):
                cell["status"].config(text=self.t("sort_table_ok"), fg="#2E7D32")
                n_correct += 1
            else:
                cell["status"].config(
                    text=self.t("sort_table_ko", ans=expected), fg="#C62828",
                )
                n_wrong += 1
                error_lines.append((
                    self.t("sort_table_err_wrong",
                           algo=algo_name, col=col_label, ans=expected, user=user_val),
                    "wrong",
                ))

        self.answered = True
        self.btn_verify.config(state=tk.DISABLED)
        for cell in self.cells.values():
            cell["combobox"].config(state=tk.DISABLED)

        if n_wrong == 0 and n_empty == 0:
            self.lbl_feedback.config(
                text=self.t("sort_table_perfect", total=n_total), fg="#4CAF50",
            )
        else:
            color = "#C62828" if n_wrong > 0 else "#FB8C00"
            self.lbl_feedback.config(
                text=self.t("sort_table_summary_done",
                            correct=n_correct, wrong=n_wrong,
                            empty=n_empty, total=n_total),
                fg=color,
            )

        if error_lines:
            self.errors_frame.pack(fill=tk.X, padx=20, pady=(0, 6))
            self.text_errors.configure(state=tk.NORMAL)
            self.text_errors.delete("1.0", tk.END)
            for line, tag in error_lines:
                self.text_errors.insert(tk.END, line + "\n", tag)
            self.text_errors.configure(state=tk.DISABLED)
        else:
            self.errors_frame.pack_forget()

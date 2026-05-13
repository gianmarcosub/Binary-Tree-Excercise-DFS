import tkinter as tk
from tkinter import ttk


SORT_TABLE_TRANSLATIONS = {
    "it": {
        "menu_sort_table": "Tabella Muta degli Ordinamenti\nCompila tutta la tabella di complessità",
        "sort_table_title": "Tabella Muta — Algoritmi di Ordinamento",
        "sort_table_intro": "Compila la tabella muta inserendo per ogni algoritmo: caso migliore, medio, peggiore, memoria, se è stabile e se è in-place.",
        "sort_table_col_algo": "Nome",
        "sort_table_col_best": "Migliore",
        "sort_table_col_avg": "Medio",
        "sort_table_col_worst": "Peggiore",
        "sort_table_col_memory": "Memoria",
        "sort_table_col_stable": "Stabile",
        "sort_table_col_inplace": "In place",
        "sort_table_verify": "Verifica",
        "sort_table_reset": "Reset",
        "sort_table_pick": "—",
        "sort_table_perfect": "✅ TABELLA COMPLETA! Tutte le {total} caselle sono corrette.",
        "sort_table_partial": "❌ {wrong}/{total} caselle errate. Le caselle sbagliate mostrano la risposta corretta.",
        "sort_table_empty": "⚠ Compila tutte le caselle prima di verificare.",
        "sort_table_ok": "✓",
        "sort_table_ko": "✗ {ans}",
    },
    "en": {
        "menu_sort_table": "Blank Sorting Table\nFill the whole complexity table",
        "sort_table_title": "Blank Table — Sorting Algorithms",
        "sort_table_intro": "Fill the blank table by entering for each algorithm: best, average, worst case, memory, whether it is stable and in-place.",
        "sort_table_col_algo": "Name",
        "sort_table_col_best": "Best",
        "sort_table_col_avg": "Average",
        "sort_table_col_worst": "Worst",
        "sort_table_col_memory": "Memory",
        "sort_table_col_stable": "Stable",
        "sort_table_col_inplace": "In place",
        "sort_table_verify": "Check",
        "sort_table_reset": "Reset",
        "sort_table_pick": "—",
        "sort_table_perfect": "✅ TABLE COMPLETE! All {total} cells are correct.",
        "sort_table_partial": "❌ {wrong}/{total} cells wrong. Wrong cells show the correct answer.",
        "sort_table_empty": "⚠ Fill all cells before checking.",
        "sort_table_ok": "✓",
        "sort_table_ko": "✗ {ans}",
    },
    "es": {
        "menu_sort_table": "Tabla Muda de Ordenación\nRellena toda la tabla de complejidad",
        "sort_table_title": "Tabla Muda — Algoritmos de Ordenación",
        "sort_table_intro": "Rellena la tabla muda introduciendo para cada algoritmo: mejor caso, caso medio, peor caso, memoria, si es estable y si es in-place.",
        "sort_table_col_algo": "Nombre",
        "sort_table_col_best": "Mejor",
        "sort_table_col_avg": "Medio",
        "sort_table_col_worst": "Peor",
        "sort_table_col_memory": "Memoria",
        "sort_table_col_stable": "Estable",
        "sort_table_col_inplace": "In place",
        "sort_table_verify": "Comprobar",
        "sort_table_reset": "Reset",
        "sort_table_pick": "—",
        "sort_table_perfect": "✅ ¡TABLA COMPLETA! Las {total} casillas son correctas.",
        "sort_table_partial": "❌ {wrong}/{total} casillas erróneas. Las erróneas muestran la respuesta correcta.",
        "sort_table_empty": "⚠ Rellena todas las casillas antes de comprobar.",
        "sort_table_ok": "✓",
        "sort_table_ko": "✗ {ans}",
    },
    "fr": {
        "menu_sort_table": "Tableau Muet des Tris\nRemplis toute la table de complexité",
        "sort_table_title": "Tableau Muet — Algorithmes de Tri",
        "sort_table_intro": "Remplis le tableau muet en indiquant pour chaque algorithme: meilleur cas, cas moyen, pire cas, mémoire, s'il est stable et s'il est in-place.",
        "sort_table_col_algo": "Nom",
        "sort_table_col_best": "Meilleur",
        "sort_table_col_avg": "Moyen",
        "sort_table_col_worst": "Pire",
        "sort_table_col_memory": "Mémoire",
        "sort_table_col_stable": "Stable",
        "sort_table_col_inplace": "In place",
        "sort_table_verify": "Vérifier",
        "sort_table_reset": "Reset",
        "sort_table_pick": "—",
        "sort_table_perfect": "✅ TABLEAU COMPLET! Les {total} cases sont correctes.",
        "sort_table_partial": "❌ {wrong}/{total} cases fausses. Les fausses affichent la bonne réponse.",
        "sort_table_empty": "⚠ Remplis toutes les cases avant de vérifier.",
        "sort_table_ok": "✓",
        "sort_table_ko": "✗ {ans}",
    },
    "de": {
        "menu_sort_table": "Leere Sortier-Tabelle\nFülle die ganze Komplexitätstabelle aus",
        "sort_table_title": "Leere Tabelle — Sortieralgorithmen",
        "sort_table_intro": "Fülle die leere Tabelle aus mit für jeden Algorithmus: bester Fall, Durchschnitt, schlechtester Fall, Speicher, ob stabil und ob in-place.",
        "sort_table_col_algo": "Name",
        "sort_table_col_best": "Bester",
        "sort_table_col_avg": "Durchschn.",
        "sort_table_col_worst": "Schlechtester",
        "sort_table_col_memory": "Speicher",
        "sort_table_col_stable": "Stabil",
        "sort_table_col_inplace": "In place",
        "sort_table_verify": "Prüfen",
        "sort_table_reset": "Reset",
        "sort_table_pick": "—",
        "sort_table_perfect": "✅ TABELLE FERTIG! Alle {total} Felder sind richtig.",
        "sort_table_partial": "❌ {wrong}/{total} Felder falsch. Falsche Felder zeigen die richtige Antwort.",
        "sort_table_empty": "⚠ Fülle alle Felder aus, bevor du prüfst.",
        "sort_table_ok": "✓",
        "sort_table_ko": "✗ {ans}",
    },
    "pt": {
        "menu_sort_table": "Tabela em Branco dos Ordenamentos\nPreencha a tabela de complexidade inteira",
        "sort_table_title": "Tabela em Branco — Algoritmos de Ordenação",
        "sort_table_intro": "Preencha a tabela em branco indicando para cada algoritmo: melhor caso, caso médio, pior caso, memória, se é estável e se é in-place.",
        "sort_table_col_algo": "Nome",
        "sort_table_col_best": "Melhor",
        "sort_table_col_avg": "Médio",
        "sort_table_col_worst": "Pior",
        "sort_table_col_memory": "Memória",
        "sort_table_col_stable": "Estável",
        "sort_table_col_inplace": "In place",
        "sort_table_verify": "Verificar",
        "sort_table_reset": "Reset",
        "sort_table_pick": "—",
        "sort_table_perfect": "✅ TABELA COMPLETA! Todas as {total} células estão corretas.",
        "sort_table_partial": "❌ {wrong}/{total} células erradas. As erradas mostram a resposta correta.",
        "sort_table_empty": "⚠ Preencha todas as células antes de verificar.",
        "sort_table_ok": "✓",
        "sort_table_ko": "✗ {ans}",
    },
}


SORT_TABLE_DATA = [
    ("Bubble sort",    "Θ(n)",         "Θ(n²)",        "Θ(n²)",        "Θ(1)", True,  True),
    ("Heap sort",      "O(n log₂ n)",  "O(n log₂ n)",  "O(n log₂ n)",  "Θ(1)", False, True),
    ("Insertion sort", "Θ(n)",         "Θ(n²)",        "Θ(n²)",        "Θ(1)", True,  True),
    ("Merge sort",     "Θ(n log₂ n)",  "Θ(n log₂ n)",  "Θ(n log₂ n)",  "O(n)", True,  False),
    ("Quick sort",     "Θ(n log₂ n)",  "Θ(n log₂ n)",  "O(n²)",        "O(n)", False, True),
    ("Selection sort", "Θ(n²)",        "Θ(n²)",        "Θ(n²)",        "Θ(1)", False, True),
]

BEST_OPTIONS = ["Θ(n)", "Θ(n²)", "Θ(n log₂ n)", "O(n log₂ n)"]
AVG_OPTIONS = ["Θ(n²)", "Θ(n log₂ n)", "O(n log₂ n)"]
WORST_OPTIONS = ["Θ(n²)", "Θ(n log₂ n)", "O(n²)", "O(n log₂ n)"]
MEMORY_OPTIONS = ["Θ(1)", "O(n)", "O(log₂ n)"]

COLUMNS_SPEC = [
    ("best",     "sort_table_col_best",    BEST_OPTIONS,   "value",  14),
    ("avg",      "sort_table_col_avg",     AVG_OPTIONS,    "value",  14),
    ("worst",    "sort_table_col_worst",   WORST_OPTIONS,  "value",  14),
    ("memory",   "sort_table_col_memory",  MEMORY_OPTIONS, "value",  11),
    ("stable",   "sort_table_col_stable",  None,           "yesno",   7),
    ("in_place", "sort_table_col_inplace", None,           "yesno",   7),
]

ROW_BG_LIGHT = "#FFFFFF"
ROW_BG_DARK = "#F4F4F4"
HEADER_BG = "#FFF8E1"
GRID_BG = "#cccccc"


class SortingTableScreen(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root, bg="#f0f0f0")
        self.controller = controller
        self.cells = {}
        self.header_labels = []
        self.name_labels = []
        self.answered = False
        self._build_ui()
        self._apply_language()

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

        self.btn_verify = tk.Button(
            top, command=self.verifica, bg="#2196F3", fg="white",
            font=("Arial", 10, "bold"), padx=10,
        )
        self.btn_verify.pack(side=tk.RIGHT, padx=5)

        self.btn_reset = tk.Button(
            top, command=self._reset_table, bg="#607D8B", fg="white",
            font=("Arial", 10, "bold"), padx=10,
        )
        self.btn_reset.pack(side=tk.RIGHT, padx=5)

        self.lbl_intro = tk.Label(
            self, text="", bg="#f0f0f0", font=("Arial", 11), fg="#333",
            wraplength=1050, justify="center",
        )
        self.lbl_intro.pack(pady=(8, 12), padx=20)

        table_outer = tk.Frame(self, bg=GRID_BG, bd=0)
        table_outer.pack(padx=20, pady=4)

        table = tk.Frame(table_outer, bg=GRID_BG)
        table.pack(padx=1, pady=1)

        # Header row
        header_specs = [
            ("sort_table_col_algo", 16),
            *[(spec[1], spec[4]) for spec in COLUMNS_SPEC],
        ]
        for col_idx, (key, width_chars) in enumerate(header_specs):
            lbl = tk.Label(
                table, bg=HEADER_BG, fg="#666",
                font=("Arial", 10, "bold", "italic"),
                anchor="center", padx=10, pady=8, width=width_chars,
            )
            lbl.grid(row=0, column=col_idx, sticky="nsew", padx=1, pady=1)
            self.header_labels.append((lbl, key))

        # Data rows
        for row_idx, row_data in enumerate(SORT_TABLE_DATA):
            algo_name = row_data[0]
            grid_row = row_idx + 1
            row_bg = ROW_BG_LIGHT if grid_row % 2 == 1 else ROW_BG_DARK

            name_lbl = tk.Label(
                table, text=algo_name, bg=row_bg, fg="#333",
                font=("Arial", 10, "bold", "italic"),
                anchor="w", padx=12, pady=6, width=16,
            )
            name_lbl.grid(row=grid_row, column=0, sticky="nsew", padx=1, pady=1)
            self.name_labels.append(name_lbl)

            for col_idx, (col_key, _label_key, options, kind, width_chars) in enumerate(
                COLUMNS_SPEC, start=1
            ):
                cell_frame = tk.Frame(table, bg=row_bg, padx=4, pady=4)
                cell_frame.grid(row=grid_row, column=col_idx, sticky="nsew", padx=1, pady=1)

                var = tk.StringVar()
                cb = ttk.Combobox(
                    cell_frame, textvariable=var, state="readonly",
                    width=max(width_chars - 2, 5),
                )
                cb.pack()

                status = tk.Label(
                    cell_frame, text="", bg=row_bg,
                    font=("Arial", 9, "bold"), fg="#555",
                )
                status.pack(pady=(2, 0))

                self.cells[(row_idx, col_key)] = {
                    "var": var, "combobox": cb, "status": status,
                    "frame": cell_frame, "bg": row_bg,
                    "kind": kind, "options": options,
                }

        bottom = tk.Frame(self, bg="#f0f0f0", pady=8)
        bottom.pack(fill=tk.X, padx=10, side=tk.BOTTOM)

        self.lbl_feedback = tk.Label(
            bottom, text="", font=("Arial", 11, "bold"), bg="#f0f0f0",
            wraplength=1000, justify="center",
        )
        self.lbl_feedback.pack(pady=8)

    def _apply_language(self):
        self.btn_back.config(text=self.t("back"))
        self.lbl_lang.config(text=self.t("language"))
        self.lbl_title.config(text=self.t("sort_table_title"))
        self.lbl_intro.config(text=self.t("sort_table_intro"))
        self.btn_verify.config(text=self.t("sort_table_verify"))
        self.btn_reset.config(text=self.t("sort_table_reset"))

        lang_pairs = self.controller.language_options()
        self.cb_lang["values"] = [name for _c, name in lang_pairs]
        current_name = next(name for code, name in lang_pairs if code == self.controller.lang)
        self.var_lang.set(current_name)

        for lbl, key in self.header_labels:
            lbl.config(text=self.t(key))

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
        # After language change, reset answered state so user can interact again
        self.answered = False
        self.btn_verify.config(state=tk.NORMAL)
        for cell in self.cells.values():
            cell["combobox"].config(state="readonly")
        self.lbl_feedback.config(text="")

    def _reset_table(self):
        self.answered = False
        self.lbl_feedback.config(text="")
        placeholder = self.t("sort_table_pick")
        for cell in self.cells.values():
            cell["var"].set(placeholder)
            cell["status"].config(text="")
            cell["combobox"].config(state="readonly")
        self.btn_verify.config(state=tk.NORMAL)

    def verifica(self):
        if self.answered:
            return

        placeholder = self.t("sort_table_pick")
        for cell in self.cells.values():
            val = cell["var"].get()
            if val == placeholder or val == "":
                self.lbl_feedback.config(text=self.t("sort_table_empty"), fg="#FF9800")
                return

        yes_str = self.t("sort_yes")
        no_str = self.t("sort_no")
        col_index = {"best": 1, "avg": 2, "worst": 3, "memory": 4, "stable": 5, "in_place": 6}

        n_wrong = 0
        n_total = len(self.cells)
        for (row_idx, col_key), cell in self.cells.items():
            user_val = cell["var"].get()
            raw_expected = SORT_TABLE_DATA[row_idx][col_index[col_key]]
            if cell["kind"] == "yesno":
                expected = yes_str if raw_expected else no_str
            else:
                expected = raw_expected
            if user_val == expected:
                cell["status"].config(text=self.t("sort_table_ok"), fg="#2E7D32")
            else:
                cell["status"].config(
                    text=self.t("sort_table_ko", ans=expected), fg="#C62828",
                )
                n_wrong += 1

        self.answered = True
        self.btn_verify.config(state=tk.DISABLED)
        for cell in self.cells.values():
            cell["combobox"].config(state=tk.DISABLED)

        if n_wrong == 0:
            self.lbl_feedback.config(
                text=self.t("sort_table_perfect", total=n_total), fg="#4CAF50",
            )
        else:
            self.lbl_feedback.config(
                text=self.t("sort_table_partial", wrong=n_wrong, total=n_total), fg="#F44336",
            )

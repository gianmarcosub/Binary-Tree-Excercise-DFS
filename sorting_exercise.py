import tkinter as tk
from tkinter import ttk
import random

import stats_tracker


SORT_TRANSLATIONS = {
    "it": {
        "menu_sort": "Algoritmi di Ordinamento\nRiconoscimento + tabella di complessità",
        "sort_title": "Algoritmi di Ordinamento",
        "sort_new": "🔄 Nuovo Esercizio",
        "sort_form_question": "Riconosci l'algoritmo e compila la tabella:",
        "sort_field_algo": "Algoritmo",
        "sort_field_worst": "Caso peggiore",
        "sort_field_avg": "Caso medio",
        "sort_field_best": "Caso migliore",
        "sort_field_inplace": "In-place",
        "sort_field_stable": "Stabile",
        "sort_verify": "Verifica",
        "sort_pick_placeholder": "— scegli —",
        "sort_yes": "Sì",
        "sort_no": "No",
        "sort_all_correct": "✅ TUTTO CORRETTO! Hai indovinato tutte e 6 le voci.",
        "sort_partial": "❌ {n_wrong}/6 risposte errate. La risposta corretta è indicata accanto a ogni campo.",
        "sort_empty": "⚠ Compila tutti i campi prima di verificare.",
        "sort_ok_mark": "✓",
        "sort_ko_mark": "✗ {ans}",
        "sort_code_lang": "Linguaggio: {lang}",
        "algo_bubble": "Bubble Sort",
        "algo_selection": "Selection Sort",
        "algo_insertion": "Insertion Sort",
        "algo_merge": "Merge Sort",
        "algo_quick": "Quick Sort",
        "algo_heap": "Heap Sort",
    },
    "en": {
        "menu_sort": "Sorting Algorithms\nRecognition + complexity table",
        "sort_title": "Sorting Algorithms",
        "sort_new": "🔄 New Exercise",
        "sort_form_question": "Identify the algorithm and fill the table:",
        "sort_field_algo": "Algorithm",
        "sort_field_worst": "Worst case",
        "sort_field_avg": "Average case",
        "sort_field_best": "Best case",
        "sort_field_inplace": "In-place",
        "sort_field_stable": "Stable",
        "sort_verify": "Check",
        "sort_pick_placeholder": "— pick —",
        "sort_yes": "Yes",
        "sort_no": "No",
        "sort_all_correct": "✅ ALL CORRECT! You got all 6 fields right.",
        "sort_partial": "❌ {n_wrong}/6 wrong. The correct answer is shown next to each field.",
        "sort_empty": "⚠ Fill all fields before checking.",
        "sort_ok_mark": "✓",
        "sort_ko_mark": "✗ {ans}",
        "sort_code_lang": "Language: {lang}",
        "algo_bubble": "Bubble Sort",
        "algo_selection": "Selection Sort",
        "algo_insertion": "Insertion Sort",
        "algo_merge": "Merge Sort",
        "algo_quick": "Quick Sort",
        "algo_heap": "Heap Sort",
    },
    "es": {
        "menu_sort": "Algoritmos de Ordenación\nReconocimiento + tabla de complejidad",
        "sort_title": "Algoritmos de Ordenación",
        "sort_new": "🔄 Nuevo Ejercicio",
        "sort_form_question": "Identifica el algoritmo y completa la tabla:",
        "sort_field_algo": "Algoritmo",
        "sort_field_worst": "Peor caso",
        "sort_field_avg": "Caso medio",
        "sort_field_best": "Mejor caso",
        "sort_field_inplace": "In-place",
        "sort_field_stable": "Estable",
        "sort_verify": "Comprobar",
        "sort_pick_placeholder": "— elige —",
        "sort_yes": "Sí",
        "sort_no": "No",
        "sort_all_correct": "✅ ¡TODO CORRECTO! Acertaste las 6 casillas.",
        "sort_partial": "❌ {n_wrong}/6 incorrectas. La respuesta correcta se muestra junto a cada campo.",
        "sort_empty": "⚠ Completa todos los campos antes de comprobar.",
        "sort_ok_mark": "✓",
        "sort_ko_mark": "✗ {ans}",
        "sort_code_lang": "Lenguaje: {lang}",
        "algo_bubble": "Bubble Sort",
        "algo_selection": "Selection Sort",
        "algo_insertion": "Insertion Sort",
        "algo_merge": "Merge Sort",
        "algo_quick": "Quick Sort",
        "algo_heap": "Heap Sort",
    },
    "fr": {
        "menu_sort": "Algorithmes de Tri\nReconnaissance + tableau de complexité",
        "sort_title": "Algorithmes de Tri",
        "sort_new": "🔄 Nouvel Exercice",
        "sort_form_question": "Identifie l'algorithme et remplis le tableau:",
        "sort_field_algo": "Algorithme",
        "sort_field_worst": "Pire cas",
        "sort_field_avg": "Cas moyen",
        "sort_field_best": "Meilleur cas",
        "sort_field_inplace": "In-place",
        "sort_field_stable": "Stable",
        "sort_verify": "Vérifier",
        "sort_pick_placeholder": "— choisir —",
        "sort_yes": "Oui",
        "sort_no": "Non",
        "sort_all_correct": "✅ TOUT EST CORRECT! Tu as réussi les 6 champs.",
        "sort_partial": "❌ {n_wrong}/6 erreurs. La bonne réponse est indiquée à côté de chaque champ.",
        "sort_empty": "⚠ Remplis tous les champs avant de vérifier.",
        "sort_ok_mark": "✓",
        "sort_ko_mark": "✗ {ans}",
        "sort_code_lang": "Langage: {lang}",
        "algo_bubble": "Bubble Sort",
        "algo_selection": "Selection Sort",
        "algo_insertion": "Insertion Sort",
        "algo_merge": "Merge Sort",
        "algo_quick": "Quick Sort",
        "algo_heap": "Heap Sort",
    },
    "de": {
        "menu_sort": "Sortieralgorithmen\nErkennung + Komplexitätstabelle",
        "sort_title": "Sortieralgorithmen",
        "sort_new": "🔄 Neue Aufgabe",
        "sort_form_question": "Erkenne den Algorithmus und fülle die Tabelle aus:",
        "sort_field_algo": "Algorithmus",
        "sort_field_worst": "Schlechtester Fall",
        "sort_field_avg": "Durchschnittlich",
        "sort_field_best": "Bester Fall",
        "sort_field_inplace": "In-place",
        "sort_field_stable": "Stabil",
        "sort_verify": "Prüfen",
        "sort_pick_placeholder": "— wählen —",
        "sort_yes": "Ja",
        "sort_no": "Nein",
        "sort_all_correct": "✅ ALLES RICHTIG! Alle 6 Felder korrekt.",
        "sort_partial": "❌ {n_wrong}/6 falsch. Die richtige Antwort steht neben jedem Feld.",
        "sort_empty": "⚠ Fülle alle Felder vor dem Prüfen aus.",
        "sort_ok_mark": "✓",
        "sort_ko_mark": "✗ {ans}",
        "sort_code_lang": "Sprache: {lang}",
        "algo_bubble": "Bubble Sort",
        "algo_selection": "Selection Sort",
        "algo_insertion": "Insertion Sort",
        "algo_merge": "Merge Sort",
        "algo_quick": "Quick Sort",
        "algo_heap": "Heap Sort",
    },
    "pt": {
        "menu_sort": "Algoritmos de Ordenação\nReconhecimento + tabela de complexidade",
        "sort_title": "Algoritmos de Ordenação",
        "sort_new": "🔄 Novo Exercício",
        "sort_form_question": "Identifique o algoritmo e preencha a tabela:",
        "sort_field_algo": "Algoritmo",
        "sort_field_worst": "Pior caso",
        "sort_field_avg": "Caso médio",
        "sort_field_best": "Melhor caso",
        "sort_field_inplace": "In-place",
        "sort_field_stable": "Estável",
        "sort_verify": "Verificar",
        "sort_pick_placeholder": "— escolha —",
        "sort_yes": "Sim",
        "sort_no": "Não",
        "sort_all_correct": "✅ TUDO CORRETO! Acertou todas as 6 respostas.",
        "sort_partial": "❌ {n_wrong}/6 erradas. A resposta correta aparece ao lado de cada campo.",
        "sort_empty": "⚠ Preencha todos os campos antes de verificar.",
        "sort_ok_mark": "✓",
        "sort_ko_mark": "✗ {ans}",
        "sort_code_lang": "Linguagem: {lang}",
        "algo_bubble": "Bubble Sort",
        "algo_selection": "Selection Sort",
        "algo_insertion": "Insertion Sort",
        "algo_merge": "Merge Sort",
        "algo_quick": "Quick Sort",
        "algo_heap": "Heap Sort",
    },
}


_BUBBLE_PY = """def sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr"""

_BUBBLE_C = """void sort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int swapped = 0;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int t = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = t;
                swapped = 1;
            }
        }
        if (!swapped) break;
    }
}"""

_SELECTION_PY = """def sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr"""

_SELECTION_C = """void sort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) min_idx = j;
        }
        int t = arr[i];
        arr[i] = arr[min_idx];
        arr[min_idx] = t;
    }
}"""

_INSERTION_PY = """def sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr"""

_INSERTION_C = """void sort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}"""

_MERGE_PY = """def sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = sort(arr[:mid])
    right = sort(arr[mid:])
    return merge(left, right)


def merge(a, b):
    result, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result"""

_MERGE_C = """void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1, n2 = r - m;
    int L[n1], R[n2];
    for (int i = 0; i < n1; i++) L[i] = arr[l + i];
    for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];
    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2)
        arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void sort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        sort(arr, l, m);
        sort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}"""

_QUICK_PY = """def sort(arr, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo < hi:
        p = partition(arr, lo, hi)
        sort(arr, lo, p - 1)
        sort(arr, p + 1, hi)


def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1"""

_QUICK_C = """int partition(int arr[], int lo, int hi) {
    int pivot = arr[hi];
    int i = lo - 1;
    for (int j = lo; j < hi; j++) {
        if (arr[j] <= pivot) {
            i++;
            int t = arr[i]; arr[i] = arr[j]; arr[j] = t;
        }
    }
    int t = arr[i + 1]; arr[i + 1] = arr[hi]; arr[hi] = t;
    return i + 1;
}

void sort(int arr[], int lo, int hi) {
    if (lo < hi) {
        int p = partition(arr, lo, hi);
        sort(arr, lo, p - 1);
        sort(arr, p + 1, hi);
    }
}"""

_HEAP_PY = """def sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)"""

_HEAP_C = """void heapify(int arr[], int n, int i) {
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;
    if (l < n && arr[l] > arr[largest]) largest = l;
    if (r < n && arr[r] > arr[largest]) largest = r;
    if (largest != i) {
        int t = arr[i]; arr[i] = arr[largest]; arr[largest] = t;
        heapify(arr, n, largest);
    }
}

void sort(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--) heapify(arr, n, i);
    for (int i = n - 1; i > 0; i--) {
        int t = arr[0]; arr[0] = arr[i]; arr[i] = t;
        heapify(arr, i, 0);
    }
}"""


SORT_ALGOS = {
    "bubble": {
        "name_key": "algo_bubble",
        "worst": "O(n²)",
        "avg": "O(n²)",
        "best": "O(n)",
        "in_place": True,
        "stable": True,
        "python": _BUBBLE_PY,
        "c": _BUBBLE_C,
    },
    "selection": {
        "name_key": "algo_selection",
        "worst": "O(n²)",
        "avg": "O(n²)",
        "best": "O(n²)",
        "in_place": True,
        "stable": False,
        "python": _SELECTION_PY,
        "c": _SELECTION_C,
    },
    "insertion": {
        "name_key": "algo_insertion",
        "worst": "O(n²)",
        "avg": "O(n²)",
        "best": "O(n)",
        "in_place": True,
        "stable": True,
        "python": _INSERTION_PY,
        "c": _INSERTION_C,
    },
    "merge": {
        "name_key": "algo_merge",
        "worst": "O(n log n)",
        "avg": "O(n log n)",
        "best": "O(n log n)",
        "in_place": False,
        "stable": True,
        "python": _MERGE_PY,
        "c": _MERGE_C,
    },
    "quick": {
        "name_key": "algo_quick",
        "worst": "O(n²)",
        "avg": "O(n log n)",
        "best": "O(n log n)",
        "in_place": True,
        "stable": False,
        "python": _QUICK_PY,
        "c": _QUICK_C,
    },
    "heap": {
        "name_key": "algo_heap",
        "worst": "O(n log n)",
        "avg": "O(n log n)",
        "best": "O(n log n)",
        "in_place": True,
        "stable": False,
        "python": _HEAP_PY,
        "c": _HEAP_C,
    },
}

WORST_AVG_OPTIONS = ["O(n²)", "O(n log n)"]
BEST_OPTIONS = ["O(n)", "O(n²)", "O(n log n)"]


def generate_sort_exercise(last_key=None):
    keys = list(SORT_ALGOS.keys())
    if last_key in keys and len(keys) > 1:
        keys = [k for k in keys if k != last_key]
    algo = random.choice(keys)
    code_lang = random.choice(["python", "c"])
    return {
        "algo": algo,
        "lang": code_lang,
        "code": SORT_ALGOS[algo][code_lang],
        "data": SORT_ALGOS[algo],
    }


class SortingScreen(tk.Frame):
    FIELD_KEYS = ("algo", "worst", "avg", "best", "in_place", "stable")

    def __init__(self, root, controller):
        super().__init__(root, bg="#f0f0f0")
        self.controller = controller
        self.current = None
        self.answered = False
        self.fields = {}
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
            values=[name for _code, name in lang_pairs],
        )
        self.cb_lang.pack(side=tk.LEFT, padx=(4, 15))
        self.cb_lang.bind("<<ComboboxSelected>>", self._on_language_change)

        self.lbl_title = tk.Label(top, bg="#e0e0e0", font=("Arial", 13, "bold"), fg="#333")
        self.lbl_title.pack(side=tk.LEFT, padx=20)

        self.btn_new = tk.Button(
            top, command=self.nuovo_esercizio, bg="#FF9800", fg="white",
            font=("Arial", 10, "bold"), padx=8,
        )
        self.btn_new.pack(side=tk.RIGHT, padx=5)

        body = tk.Frame(self, bg="#f0f0f0")
        body.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)
        body.columnconfigure(0, weight=3, minsize=520)
        body.columnconfigure(1, weight=2, minsize=420)
        body.rowconfigure(0, weight=1)

        code_panel = tk.Frame(body, bg="#1e1e1e", bd=2, relief=tk.SUNKEN)
        code_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 8))

        self.lbl_code_lang = tk.Label(
            code_panel, bg="#2d2d2d", fg="#dcdcdc",
            font=("Arial", 10, "bold"), pady=6, anchor="w", padx=12,
        )
        self.lbl_code_lang.pack(fill=tk.X)

        self.text_code = tk.Text(
            code_panel, font=("Consolas", 12), bg="#1e1e1e", fg="#dcdcdc",
            insertbackground="#dcdcdc", padx=14, pady=10, bd=0, wrap="none",
        )
        self.text_code.pack(expand=True, fill=tk.BOTH)
        self.text_code.configure(state=tk.DISABLED)

        form_panel = tk.Frame(body, bg="#f0f0f0")
        form_panel.grid(row=0, column=1, sticky="nsew")
        form_panel.columnconfigure(0, weight=0, minsize=130)
        form_panel.columnconfigure(1, weight=0)
        form_panel.columnconfigure(2, weight=1)

        self.lbl_question = tk.Label(
            form_panel, bg="#f0f0f0", font=("Arial", 11, "bold"), fg="#333",
            wraplength=400, justify="left", anchor="w",
        )
        self.lbl_question.grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 12))

        for row, key in enumerate(self.FIELD_KEYS, start=1):
            lbl = tk.Label(form_panel, bg="#f0f0f0", font=("Arial", 10, "bold"), anchor="w")
            lbl.grid(row=row, column=0, sticky="w", padx=(0, 8), pady=5)
            var = tk.StringVar()
            cb = ttk.Combobox(form_panel, textvariable=var, state="readonly", width=18)
            cb.grid(row=row, column=1, sticky="w", pady=5)
            status = tk.Label(
                form_panel, bg="#f0f0f0", font=("Arial", 10, "bold"), anchor="w",
            )
            status.grid(row=row, column=2, sticky="w", padx=(10, 0), pady=5)
            self.fields[key] = {"label": lbl, "combobox": cb, "var": var, "status": status}

        self.btn_verify = tk.Button(
            form_panel, command=self.verifica, bg="#2196F3", fg="white",
            font=("Arial", 11, "bold"), padx=16, pady=4,
        )
        self.btn_verify.grid(
            row=len(self.FIELD_KEYS) + 1, column=0, columnspan=3, pady=14, sticky="w",
        )

        self.lbl_feedback = tk.Label(
            form_panel, bg="#f0f0f0", font=("Arial", 11, "bold"),
            wraplength=400, justify="left", anchor="w",
        )
        self.lbl_feedback.grid(
            row=len(self.FIELD_KEYS) + 2, column=0, columnspan=3, sticky="w", pady=8,
        )

    def _label_keys(self):
        return {
            "algo": "sort_field_algo",
            "worst": "sort_field_worst",
            "avg": "sort_field_avg",
            "best": "sort_field_best",
            "in_place": "sort_field_inplace",
            "stable": "sort_field_stable",
        }

    def _apply_language(self):
        self.btn_back.config(text=self.t("back"))
        self.lbl_lang.config(text=self.t("language"))
        self.lbl_title.config(text=self.t("sort_title"))
        self.btn_new.config(text=self.t("sort_new"))
        self.lbl_question.config(text=self.t("sort_form_question"))
        self.btn_verify.config(text=self.t("sort_verify"))

        lang_pairs = self.controller.language_options()
        self.cb_lang["values"] = [name for _c, name in lang_pairs]
        current_name = next(name for code, name in lang_pairs if code == self.controller.lang)
        self.var_lang.set(current_name)

        for key, tk_key in self._label_keys().items():
            self.fields[key]["label"].config(text=self.t(tk_key) + ":")

        placeholder = self.t("sort_pick_placeholder")
        algo_options = [placeholder] + [self.t(SORT_ALGOS[k]["name_key"]) for k in SORT_ALGOS]
        yn = [placeholder, self.t("sort_yes"), self.t("sort_no")]

        self.fields["algo"]["combobox"]["values"] = algo_options
        self.fields["worst"]["combobox"]["values"] = [placeholder] + WORST_AVG_OPTIONS
        self.fields["avg"]["combobox"]["values"] = [placeholder] + WORST_AVG_OPTIONS
        self.fields["best"]["combobox"]["values"] = [placeholder] + BEST_OPTIONS
        self.fields["in_place"]["combobox"]["values"] = yn
        self.fields["stable"]["combobox"]["values"] = yn

        for key in self.FIELD_KEYS:
            self.fields[key]["var"].set(placeholder)
            self.fields[key]["status"].config(text="")

        if self.current:
            lang_disp = "Python" if self.current["lang"] == "python" else "C"
            self.lbl_code_lang.config(text=self.t("sort_code_lang", lang=lang_disp))

    def _on_language_change(self, _e=None):
        chosen = self.var_lang.get()
        for code, name in self.controller.language_options():
            if name == chosen:
                self.controller.set_language(code)
                break
        self._apply_language()
        # After language change, re-enable the form and clear feedback
        self.answered = False
        self.btn_verify.config(state=tk.NORMAL)
        for key in self.FIELD_KEYS:
            self.fields[key]["combobox"].config(state="readonly")
        self.lbl_feedback.config(text="")

    def nuovo_esercizio(self):
        self.answered = False
        self.lbl_feedback.config(text="")
        self.btn_verify.config(state=tk.NORMAL)

        placeholder = self.t("sort_pick_placeholder")
        for key in self.FIELD_KEYS:
            self.fields[key]["var"].set(placeholder)
            self.fields[key]["status"].config(text="")
            self.fields[key]["combobox"].config(state="readonly")

        last = self.current["algo"] if self.current else None
        self.current = generate_sort_exercise(last_key=last)

        self.text_code.configure(state=tk.NORMAL)
        self.text_code.delete("1.0", tk.END)
        self.text_code.insert("1.0", self.current["code"])
        self.text_code.configure(state=tk.DISABLED)

        lang_disp = "Python" if self.current["lang"] == "python" else "C"
        self.lbl_code_lang.config(text=self.t("sort_code_lang", lang=lang_disp))

    def verifica(self):
        if self.answered or self.current is None:
            return

        placeholder = self.t("sort_pick_placeholder")
        for key in self.FIELD_KEYS:
            if self.fields[key]["var"].get() == placeholder:
                self.lbl_feedback.config(text=self.t("sort_empty"), fg="#FF9800")
                return

        data = self.current["data"]
        yes_str = self.t("sort_yes")
        no_str = self.t("sort_no")

        expected = {
            "algo": self.t(data["name_key"]),
            "worst": data["worst"],
            "avg": data["avg"],
            "best": data["best"],
            "in_place": yes_str if data["in_place"] else no_str,
            "stable": yes_str if data["stable"] else no_str,
        }

        n_wrong = 0
        for key in self.FIELD_KEYS:
            user_val = self.fields[key]["var"].get()
            correct_val = expected[key]
            if user_val == correct_val:
                self.fields[key]["status"].config(text=self.t("sort_ok_mark"), fg="#4CAF50")
            else:
                self.fields[key]["status"].config(
                    text=self.t("sort_ko_mark", ans=correct_val), fg="#F44336",
                )
                n_wrong += 1

        self.answered = True
        self.btn_verify.config(state=tk.DISABLED)
        for key in self.FIELD_KEYS:
            self.fields[key]["combobox"].config(state=tk.DISABLED)

        stats_tracker.record("sort", n_wrong == 0)

        if n_wrong == 0:
            self.lbl_feedback.config(text=self.t("sort_all_correct"), fg="#4CAF50")
        else:
            self.lbl_feedback.config(
                text=self.t("sort_partial", n_wrong=n_wrong), fg="#F44336",
            )

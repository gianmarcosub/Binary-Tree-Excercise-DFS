import tkinter as tk
import random

import stats_tracker


RANDOM_MIX_TRANSLATIONS = {
    "it": {
        "menu_random": "Esercizio Random\nEstrae a sorte tra tutti gli esercizi",
        "random_next": "🎲 Prossimo Random",
    },
    "en": {
        "menu_random": "Random Exercise\nPick at random from all exercises",
        "random_next": "🎲 Next Random",
    },
    "es": {
        "menu_random": "Ejercicio Aleatorio\nElige al azar entre todos los ejercicios",
        "random_next": "🎲 Siguiente Aleatorio",
    },
    "fr": {
        "menu_random": "Exercice Aléatoire\nTire au sort parmi tous les exercices",
        "random_next": "🎲 Prochain Aléatoire",
    },
    "de": {
        "menu_random": "Zufallsaufgabe\nZufällig aus allen Übungen wählen",
        "random_next": "🎲 Nächste Zufallsaufgabe",
    },
    "pt": {
        "menu_random": "Exercício Aleatório\nSorteia entre todos os exercícios",
        "random_next": "🎲 Próximo Aleatório",
    },
}


class RandomMixScreen(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root, bg="#f0f0f0")
        self.controller = controller
        self.sub_screen = None
        self.last_key = None
        self._choices = None
        self._pick_and_show()

    def _build_choices(self):
        # Lazy import to avoid circular dependency with main.py.
        from main import DFSScreen, RBScreen, AsyncScreen, SortingScreen
        from bfs_exercise import BFSScreen
        from sort_table_row_exercise import SortTableRowScreen

        # key -> (screen_class, attribute name of the "new exercise" button to rebind)
        self._choices = {
            "dfs":      (DFSScreen,          "btn_genera"),
            "bfs":      (BFSScreen,          "btn_genera"),
            "rb":       (RBScreen,           "btn_new"),
            "async":    (AsyncScreen,        "btn_new"),
            "sort":     (SortingScreen,      "btn_new"),
            "sort_row": (SortTableRowScreen, "btn_new"),
        }

    def _pick_and_show(self):
        if self._choices is None:
            self._build_choices()

        keys = list(self._choices.keys())
        if self.last_key in keys and len(keys) > 1:
            keys = [k for k in keys if k != self.last_key]

        weights = stats_tracker.weights(keys)
        if weights and any(w > 0 for w in weights):
            chosen = random.choices(keys, weights=weights, k=1)[0]
        else:
            chosen = random.choice(keys)
        self.last_key = chosen

        if self.sub_screen is not None:
            self.sub_screen.destroy()

        cls, button_attr = self._choices[chosen]
        self.sub_screen = cls(self, self.controller)
        self.sub_screen.pack(expand=True, fill=tk.BOTH)

        # Rebind the sub-screen's "new exercise" button to advance to next random.
        btn = getattr(self.sub_screen, button_attr, None)
        if btn is not None:
            btn.config(
                command=self._pick_and_show,
                text=self.controller.t("random_next"),
            )

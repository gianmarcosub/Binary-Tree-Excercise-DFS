import tkinter as tk
from tkinter import ttk
import random
import math
import heapq
from collections import deque

import stats_tracker


GRAPH_TRANSLATIONS = {
    "it": {
        "menu_graph": "Grafi\nDijkstra · Bellman-Ford · Kosaraju · Erdős",
        "graph_menu_title": "Esercizi su Grafi",
        "graph_menu_subtitle": "Scegli un algoritmo",
        "graph_dijkstra": "Dijkstra\nCammini minimi (pesi ≥ 0)",
        "graph_bellman": "Bellman-Ford\nCammini minimi (anche pesi negativi)",
        "graph_kosaraju": "Kosaraju\nComponenti fortemente connesse (SCC)",
        "graph_erdos": "Numero di Erdős\nDistanze BFS in grafo non pesato",
        "graph_back": "← Indietro",
        "graph_back_menu": "← Menu principale",
        "graph_new": "🔄 Nuovo grafo",
        "graph_verify": "Verifica",
        "graph_your_answer": "Risposta:",
        "graph_correct": "✅ ESATTO!",
        "graph_wrong_full": "❌ Sbagliato.\nLa tua: {user}\nCorretta: {correct}",
        "graph_format_error": "⚠ Formato non valido. Usa numeri separati da virgola (e 'inf' per infinito).",
        "graph_empty": "⚠ Inserisci la risposta prima di verificare.",
        "dijkstra_title": "Dijkstra — Cammini Minimi",
        "dijkstra_mission": "Sorgente: nodo {src}. Scrivi la distanza minima verso i nodi {nodes}, separate da virgola. Usa 'inf' se il nodo non è raggiungibile.",
        "bellman_title": "Bellman-Ford — Cammini Minimi",
        "bellman_mission": "Sorgente: nodo {src}. Distanze minime verso {nodes} (virgole). Se rilevi un ciclo negativo raggiungibile dalla sorgente premi il pulsante.",
        "bellman_neg_cycle_btn": "⚠ Ciclo negativo",
        "bellman_neg_cycle_true": "✅ ESATTO! C'è un ciclo negativo raggiungibile dalla sorgente.",
        "bellman_neg_cycle_false": "❌ Sbagliato. Non c'è un ciclo negativo raggiungibile dalla sorgente.\nDistanze corrette: {correct}",
        "bellman_neg_cycle_missed": "❌ Sbagliato. C'era un ciclo negativo raggiungibile dalla sorgente.",
        "kosaraju_title": "Kosaraju — Componenti Fortemente Connesse",
        "kosaraju_mission": "Identifica le SCC. Nodi della stessa SCC separati da virgola, SCC diverse separate da '|'.  Esempio: 1,2,3 | 4 | 5,6",
        "erdos_title": "Numero di Erdős",
        "erdos_mission": "Erdős è il nodo {src}. Scrivi il numero di Erdős dei nodi {nodes} separati da virgola (usa 'inf' per non raggiungibili).",
        "cat_dijkstra": "Grafi - Dijkstra",
        "cat_bellman": "Grafi - Bellman-Ford",
        "cat_kosaraju": "Grafi - Kosaraju (SCC)",
        "cat_erdos": "Grafi - Numero di Erdős",
    },
    "en": {
        "menu_graph": "Graphs\nDijkstra · Bellman-Ford · Kosaraju · Erdős",
        "graph_menu_title": "Graph Exercises",
        "graph_menu_subtitle": "Pick an algorithm",
        "graph_dijkstra": "Dijkstra\nShortest paths (weights ≥ 0)",
        "graph_bellman": "Bellman-Ford\nShortest paths (negative weights allowed)",
        "graph_kosaraju": "Kosaraju\nStrongly Connected Components (SCC)",
        "graph_erdos": "Erdős Number\nBFS distances in an unweighted graph",
        "graph_back": "← Back",
        "graph_back_menu": "← Main menu",
        "graph_new": "🔄 New graph",
        "graph_verify": "Check",
        "graph_your_answer": "Answer:",
        "graph_correct": "✅ CORRECT!",
        "graph_wrong_full": "❌ Wrong.\nYours: {user}\nCorrect: {correct}",
        "graph_format_error": "⚠ Invalid format. Use comma-separated numbers (and 'inf' for infinity).",
        "graph_empty": "⚠ Enter your answer before checking.",
        "dijkstra_title": "Dijkstra — Shortest Paths",
        "dijkstra_mission": "Source: node {src}. Enter the minimum distance to nodes {nodes}, comma-separated. Use 'inf' if unreachable.",
        "bellman_title": "Bellman-Ford — Shortest Paths",
        "bellman_mission": "Source: node {src}. Minimum distances to {nodes} (commas). Press the button if you detect a reachable negative cycle.",
        "bellman_neg_cycle_btn": "⚠ Negative cycle",
        "bellman_neg_cycle_true": "✅ CORRECT! There is a negative cycle reachable from the source.",
        "bellman_neg_cycle_false": "❌ Wrong. There is no reachable negative cycle.\nCorrect distances: {correct}",
        "bellman_neg_cycle_missed": "❌ Wrong. There was a negative cycle reachable from the source.",
        "kosaraju_title": "Kosaraju — Strongly Connected Components",
        "kosaraju_mission": "Identify the SCCs. Nodes inside one SCC separated by commas, different SCCs separated by '|'. E.g.: 1,2,3 | 4 | 5,6",
        "erdos_title": "Erdős Number",
        "erdos_mission": "Erdős is node {src}. Enter the Erdős number of nodes {nodes}, comma-separated (use 'inf' for unreachable).",
        "cat_dijkstra": "Graphs - Dijkstra",
        "cat_bellman": "Graphs - Bellman-Ford",
        "cat_kosaraju": "Graphs - Kosaraju (SCC)",
        "cat_erdos": "Graphs - Erdős Number",
    },
    "es": {
        "menu_graph": "Grafos\nDijkstra · Bellman-Ford · Kosaraju · Erdős",
        "graph_menu_title": "Ejercicios de Grafos",
        "graph_menu_subtitle": "Elige un algoritmo",
        "graph_dijkstra": "Dijkstra\nCaminos mínimos (pesos ≥ 0)",
        "graph_bellman": "Bellman-Ford\nCaminos mínimos (pesos negativos admitidos)",
        "graph_kosaraju": "Kosaraju\nComponentes fuertemente conexas (SCC)",
        "graph_erdos": "Número de Erdős\nDistancias BFS en grafo no ponderado",
        "graph_back": "← Atrás",
        "graph_back_menu": "← Menú principal",
        "graph_new": "🔄 Nuevo grafo",
        "graph_verify": "Comprobar",
        "graph_your_answer": "Respuesta:",
        "graph_correct": "✅ ¡CORRECTO!",
        "graph_wrong_full": "❌ Incorrecto.\nTuya: {user}\nCorrecta: {correct}",
        "graph_format_error": "⚠ Formato inválido. Usa números separados por coma (y 'inf' para infinito).",
        "graph_empty": "⚠ Introduce la respuesta antes de comprobar.",
        "dijkstra_title": "Dijkstra — Caminos Mínimos",
        "dijkstra_mission": "Fuente: nodo {src}. Distancia mínima a los nodos {nodes}, separadas por comas. Usa 'inf' si no es alcanzable.",
        "bellman_title": "Bellman-Ford — Caminos Mínimos",
        "bellman_mission": "Fuente: nodo {src}. Distancias mínimas a {nodes} (comas). Si detectas un ciclo negativo alcanzable, pulsa el botón.",
        "bellman_neg_cycle_btn": "⚠ Ciclo negativo",
        "bellman_neg_cycle_true": "✅ ¡CORRECTO! Hay un ciclo negativo alcanzable desde la fuente.",
        "bellman_neg_cycle_false": "❌ Incorrecto. No hay ciclo negativo alcanzable.\nDistancias correctas: {correct}",
        "bellman_neg_cycle_missed": "❌ Incorrecto. Había un ciclo negativo alcanzable desde la fuente.",
        "kosaraju_title": "Kosaraju — Componentes Fuertemente Conexas",
        "kosaraju_mission": "Identifica las SCC. Nodos de la misma SCC separados por comas, SCC distintas separadas por '|'. Ej.: 1,2,3 | 4 | 5,6",
        "erdos_title": "Número de Erdős",
        "erdos_mission": "Erdős es el nodo {src}. Escribe el número de Erdős de los nodos {nodes} separados por comas (usa 'inf' para no alcanzables).",
        "cat_dijkstra": "Grafos - Dijkstra",
        "cat_bellman": "Grafos - Bellman-Ford",
        "cat_kosaraju": "Grafos - Kosaraju (SCC)",
        "cat_erdos": "Grafos - Número de Erdős",
    },
    "fr": {
        "menu_graph": "Graphes\nDijkstra · Bellman-Ford · Kosaraju · Erdős",
        "graph_menu_title": "Exercices sur les Graphes",
        "graph_menu_subtitle": "Choisis un algorithme",
        "graph_dijkstra": "Dijkstra\nPlus courts chemins (poids ≥ 0)",
        "graph_bellman": "Bellman-Ford\nPlus courts chemins (poids négatifs admis)",
        "graph_kosaraju": "Kosaraju\nComposantes fortement connexes (SCC)",
        "graph_erdos": "Nombre d'Erdős\nDistances BFS dans un graphe non pondéré",
        "graph_back": "← Retour",
        "graph_back_menu": "← Menu principal",
        "graph_new": "🔄 Nouveau graphe",
        "graph_verify": "Vérifier",
        "graph_your_answer": "Réponse :",
        "graph_correct": "✅ CORRECT !",
        "graph_wrong_full": "❌ Faux.\nLa tienne : {user}\nCorrecte : {correct}",
        "graph_format_error": "⚠ Format invalide. Utilise des nombres séparés par des virgules (et 'inf' pour l'infini).",
        "graph_empty": "⚠ Entre une réponse avant de vérifier.",
        "dijkstra_title": "Dijkstra — Plus Courts Chemins",
        "dijkstra_mission": "Source : nœud {src}. Distance minimale vers {nodes}, séparées par des virgules. Utilise 'inf' si inaccessible.",
        "bellman_title": "Bellman-Ford — Plus Courts Chemins",
        "bellman_mission": "Source : nœud {src}. Distances minimales vers {nodes} (virgules). Si tu détectes un cycle négatif accessible, appuie sur le bouton.",
        "bellman_neg_cycle_btn": "⚠ Cycle négatif",
        "bellman_neg_cycle_true": "✅ CORRECT ! Il existe un cycle négatif accessible depuis la source.",
        "bellman_neg_cycle_false": "❌ Faux. Aucun cycle négatif accessible.\nDistances correctes : {correct}",
        "bellman_neg_cycle_missed": "❌ Faux. Il y avait un cycle négatif accessible depuis la source.",
        "kosaraju_title": "Kosaraju — Composantes Fortement Connexes",
        "kosaraju_mission": "Identifie les SCC. Nœuds d'une même SCC séparés par des virgules, SCC distinctes séparées par '|'. Ex. : 1,2,3 | 4 | 5,6",
        "erdos_title": "Nombre d'Erdős",
        "erdos_mission": "Erdős est le nœud {src}. Écris le nombre d'Erdős des nœuds {nodes} séparés par des virgules (utilise 'inf' pour inaccessibles).",
        "cat_dijkstra": "Graphes - Dijkstra",
        "cat_bellman": "Graphes - Bellman-Ford",
        "cat_kosaraju": "Graphes - Kosaraju (SCC)",
        "cat_erdos": "Graphes - Nombre d'Erdős",
    },
    "de": {
        "menu_graph": "Graphen\nDijkstra · Bellman-Ford · Kosaraju · Erdős",
        "graph_menu_title": "Graph-Übungen",
        "graph_menu_subtitle": "Wähle einen Algorithmus",
        "graph_dijkstra": "Dijkstra\nKürzeste Pfade (Gewichte ≥ 0)",
        "graph_bellman": "Bellman-Ford\nKürzeste Pfade (auch negative Gewichte)",
        "graph_kosaraju": "Kosaraju\nStark zusammenhängende Komponenten (SCC)",
        "graph_erdos": "Erdős-Zahl\nBFS-Distanzen in ungewichtetem Graph",
        "graph_back": "← Zurück",
        "graph_back_menu": "← Hauptmenü",
        "graph_new": "🔄 Neuer Graph",
        "graph_verify": "Prüfen",
        "graph_your_answer": "Antwort:",
        "graph_correct": "✅ RICHTIG!",
        "graph_wrong_full": "❌ Falsch.\nDeine: {user}\nRichtig: {correct}",
        "graph_format_error": "⚠ Ungültiges Format. Zahlen durch Komma trennen (und 'inf' für Unendlich).",
        "graph_empty": "⚠ Antwort eingeben, bevor du prüfst.",
        "dijkstra_title": "Dijkstra — Kürzeste Pfade",
        "dijkstra_mission": "Quelle: Knoten {src}. Minimale Distanz zu Knoten {nodes}, durch Komma getrennt. 'inf' wenn unerreichbar.",
        "bellman_title": "Bellman-Ford — Kürzeste Pfade",
        "bellman_mission": "Quelle: Knoten {src}. Minimale Distanzen zu {nodes} (Kommas). Bei erreichbarem negativen Kreis Button drücken.",
        "bellman_neg_cycle_btn": "⚠ Negativer Kreis",
        "bellman_neg_cycle_true": "✅ RICHTIG! Es gibt einen von der Quelle erreichbaren negativen Kreis.",
        "bellman_neg_cycle_false": "❌ Falsch. Kein erreichbarer negativer Kreis.\nRichtige Distanzen: {correct}",
        "bellman_neg_cycle_missed": "❌ Falsch. Es gab einen erreichbaren negativen Kreis.",
        "kosaraju_title": "Kosaraju — Stark Zusammenhängende Komponenten",
        "kosaraju_mission": "Identifiziere die SCCs. Knoten derselben SCC durch Komma, verschiedene SCCs durch '|'. Z.B.: 1,2,3 | 4 | 5,6",
        "erdos_title": "Erdős-Zahl",
        "erdos_mission": "Erdős ist Knoten {src}. Erdős-Zahl der Knoten {nodes}, durch Komma getrennt ('inf' für unerreichbar).",
        "cat_dijkstra": "Graphen - Dijkstra",
        "cat_bellman": "Graphen - Bellman-Ford",
        "cat_kosaraju": "Graphen - Kosaraju (SCC)",
        "cat_erdos": "Graphen - Erdős-Zahl",
    },
    "pt": {
        "menu_graph": "Grafos\nDijkstra · Bellman-Ford · Kosaraju · Erdős",
        "graph_menu_title": "Exercícios de Grafos",
        "graph_menu_subtitle": "Escolha um algoritmo",
        "graph_dijkstra": "Dijkstra\nCaminhos mínimos (pesos ≥ 0)",
        "graph_bellman": "Bellman-Ford\nCaminhos mínimos (pesos negativos permitidos)",
        "graph_kosaraju": "Kosaraju\nComponentes fortemente conexos (SCC)",
        "graph_erdos": "Número de Erdős\nDistâncias BFS em grafo não ponderado",
        "graph_back": "← Voltar",
        "graph_back_menu": "← Menu principal",
        "graph_new": "🔄 Novo grafo",
        "graph_verify": "Verificar",
        "graph_your_answer": "Resposta:",
        "graph_correct": "✅ CORRETO!",
        "graph_wrong_full": "❌ Errado.\nSua: {user}\nCorreta: {correct}",
        "graph_format_error": "⚠ Formato inválido. Use números separados por vírgula (e 'inf' para infinito).",
        "graph_empty": "⚠ Insira a resposta antes de verificar.",
        "dijkstra_title": "Dijkstra — Caminhos Mínimos",
        "dijkstra_mission": "Fonte: nó {src}. Distância mínima até os nós {nodes}, separadas por vírgulas. Use 'inf' se inalcançável.",
        "bellman_title": "Bellman-Ford — Caminhos Mínimos",
        "bellman_mission": "Fonte: nó {src}. Distâncias mínimas até {nodes} (vírgulas). Se detectar ciclo negativo alcançável, clique no botão.",
        "bellman_neg_cycle_btn": "⚠ Ciclo negativo",
        "bellman_neg_cycle_true": "✅ CORRETO! Há um ciclo negativo alcançável desde a fonte.",
        "bellman_neg_cycle_false": "❌ Errado. Não há ciclo negativo alcançável.\nDistâncias corretas: {correct}",
        "bellman_neg_cycle_missed": "❌ Errado. Havia um ciclo negativo alcançável desde a fonte.",
        "kosaraju_title": "Kosaraju — Componentes Fortemente Conexos",
        "kosaraju_mission": "Identifique os SCCs. Nós no mesmo SCC separados por vírgulas, SCCs distintos separados por '|'. Ex.: 1,2,3 | 4 | 5,6",
        "erdos_title": "Número de Erdős",
        "erdos_mission": "Erdős é o nó {src}. Escreva o número de Erdős dos nós {nodes} separados por vírgulas (use 'inf' para inalcançáveis).",
        "cat_dijkstra": "Grafos - Dijkstra",
        "cat_bellman": "Grafos - Bellman-Ford",
        "cat_kosaraju": "Grafos - Kosaraju (SCC)",
        "cat_erdos": "Grafos - Número de Erdős",
    },
}


# ============================================================
# Algorithms
# ============================================================

def dijkstra(n, weighted_edges, src):
    INF = math.inf
    dist = [INF] * n
    dist[src] = 0
    adj = [[] for _ in range(n)]
    for u, v, w in weighted_edges:
        adj[u].append((v, w))
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist


def bellman_ford(n, weighted_edges, src):
    INF = math.inf
    dist = [INF] * n
    dist[src] = 0
    for _ in range(n - 1):
        updated = False
        for u, v, w in weighted_edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break
    has_neg_cycle = False
    for u, v, w in weighted_edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            has_neg_cycle = True
            break
    return dist, has_neg_cycle


def kosaraju(n, edges):
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        radj[v].append(u)
    visited = [False] * n
    order = []
    for start in range(n):
        if visited[start]:
            continue
        stack = [(start, iter(adj[start]))]
        visited[start] = True
        while stack:
            node, it = stack[-1]
            nxt = next(it, None)
            if nxt is None:
                order.append(node)
                stack.pop()
            elif not visited[nxt]:
                visited[nxt] = True
                stack.append((nxt, iter(adj[nxt])))
    component = [-1] * n
    cid = 0
    for u in reversed(order):
        if component[u] != -1:
            continue
        stack2 = [u]
        component[u] = cid
        while stack2:
            node = stack2.pop()
            for nxt in radj[node]:
                if component[nxt] == -1:
                    component[nxt] = cid
                    stack2.append(nxt)
        cid += 1
    sccs = [[] for _ in range(cid)]
    for i in range(n):
        sccs[component[i]].append(i)
    return sccs


def bfs_dist(n, adj, src):
    INF = math.inf
    dist = [INF] * n
    dist[src] = 0
    q = deque([src])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == INF:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


# ============================================================
# Random graph generation
# ============================================================

def gen_weighted_digraph(n, density=0.4, w_min=1, w_max=9):
    edges = []
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            if random.random() < density:
                edges.append((u, v, random.randint(w_min, w_max)))
    # backbone to give the source something to reach
    for u in range(n - 1):
        if not any(e[0] == u and e[1] == u + 1 for e in edges):
            edges.append((u, u + 1, random.randint(max(1, w_min), w_max)))
    return edges


def gen_unweighted_digraph(n, density=0.35):
    edges = []
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            if random.random() < density:
                edges.append((u, v))
    if not edges:
        edges.append((0, 1))
    return edges


def gen_undirected(n, density=0.35):
    edges = []
    for u in range(n):
        for v in range(u + 1, n):
            if random.random() < density:
                edges.append((u, v))
    if not edges:
        edges.append((0, 1))
    return edges


# ============================================================
# Layout
# ============================================================

def circular_layout(n, cx, cy, r):
    out = []
    for i in range(n):
        angle = 2 * math.pi * i / n - math.pi / 2
        out.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    return out


# ============================================================
# Parsing / formatting helpers
# ============================================================

def _parse_dist_list(text, expected_n):
    cleaned = text.replace(";", ",").replace("∞", "inf")
    parts = [p.strip().lower() for p in cleaned.split(",") if p.strip()]
    if len(parts) != expected_n:
        return None
    result = []
    for p in parts:
        if p in ("inf", "infty", "infinity", "+inf", "+infty"):
            result.append(math.inf)
        else:
            try:
                result.append(int(p))
            except ValueError:
                try:
                    result.append(float(p))
                except ValueError:
                    return None
    return result


def _parse_scc_groups(text):
    groups = []
    for g in text.split("|"):
        nodes = []
        for p in g.replace(";", ",").split(","):
            p = p.strip()
            if not p:
                continue
            try:
                nodes.append(int(p))
            except ValueError:
                return None
        if nodes:
            groups.append(frozenset(nodes))
    if not groups:
        return None
    return groups


def _format_dist(d):
    if d == math.inf:
        return "∞"
    if isinstance(d, float) and d.is_integer():
        return str(int(d))
    return str(d)


def _format_dist_list(distances):
    return ", ".join(_format_dist(d) for d in distances)


def _format_sccs(sccs_iterable):
    items = sorted(sccs_iterable, key=lambda s: (len(s), min(s) if s else 0))
    return " ".join(
        "{" + ",".join(str(n + 1) for n in sorted(s)) + "}" for s in items
    )


# ============================================================
# Base screen
# ============================================================

class _GraphScreenBase(tk.Frame):
    NODE_R = 22

    def __init__(self, parent, controller, on_back, stats_cat, accent_color):
        super().__init__(parent, bg="#f0f0f0")
        self.controller = controller
        self.on_back = on_back
        self.stats_cat = stats_cat
        self.accent_color = accent_color
        self.n = 0
        self.edges = []
        self.weighted = True
        self.directed = True
        self.positions = []
        self.answered = False
        self.stats_recorded = False
        self._build_ui()
        self._apply_language()
        self.new_exercise()

    def t(self, key, **fmt):
        return self.controller.t(key, **fmt)

    # ------ UI ------
    def _build_ui(self):
        top = tk.Frame(self, bg="#e0e0e0", pady=8, padx=10, relief=tk.RAISED, bd=2)
        top.pack(fill=tk.X, padx=10, pady=(10, 5))

        self.btn_back = tk.Button(
            top, command=self.on_back, bg="#757575", fg="white",
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
        self.lbl_title.pack(side=tk.LEFT, padx=15)

        self.btn_new = tk.Button(
            top, command=self.new_exercise, bg=self.accent_color, fg="white",
            font=("Arial", 10, "bold"), padx=8,
        )
        self.btn_new.pack(side=tk.RIGHT, padx=5)

        canvas_frame = tk.Frame(self, bd=2, relief=tk.SUNKEN, bg="white")
        canvas_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)
        self.canvas = tk.Canvas(canvas_frame, bg="white", highlightthickness=0)
        self.canvas.pack(expand=True, fill=tk.BOTH)
        self.canvas.bind("<Configure>", lambda _e: self._draw_graph())

        bottom = tk.Frame(self, bg="#f0f0f0", pady=8)
        bottom.pack(fill=tk.X, padx=10, side=tk.BOTTOM)

        self.lbl_mission = tk.Label(
            bottom, text="", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#333",
            wraplength=1020, justify="center",
        )
        self.lbl_mission.pack(pady=(0, 8))

        row = tk.Frame(bottom, bg="#f0f0f0")
        row.pack()
        self.lbl_answer = tk.Label(row, font=("Arial", 11), bg="#f0f0f0")
        self.lbl_answer.pack(side=tk.LEFT, padx=5)
        self.entry = tk.Entry(row, width=50, font=("Arial", 12), justify="center")
        self.entry.pack(side=tk.LEFT, padx=5)
        self.entry.bind("<Return>", lambda _e: self.verify())
        self.btn_verify = tk.Button(
            row, command=self.verify, bg="#2196F3", fg="white",
            font=("Arial", 11, "bold"), padx=10,
        )
        self.btn_verify.pack(side=tk.LEFT, padx=5)
        self._build_extra_buttons(row)

        self.lbl_feedback = tk.Label(
            bottom, text="", font=("Arial", 11, "bold"), bg="#f0f0f0",
            wraplength=1020, justify="center",
        )
        self.lbl_feedback.pack(pady=8)

    def _build_extra_buttons(self, row):
        pass

    def _apply_language(self):
        self.btn_back.config(text=self.t("graph_back"))
        self.lbl_lang.config(text=self.t("language"))
        self.btn_new.config(text=self.t("graph_new"))
        self.lbl_answer.config(text=self.t("graph_your_answer"))
        self.btn_verify.config(text=self.t("graph_verify"))
        self.lbl_title.config(text=self.t(self._title_key()))
        lang_pairs = self.controller.language_options()
        self.cb_lang["values"] = [name for _c, name in lang_pairs]
        current_name = next(name for code, name in lang_pairs if code == self.controller.lang)
        self.var_lang.set(current_name)
        self._apply_language_extra()
        self._refresh_mission()

    def _apply_language_extra(self):
        pass

    def _on_language_change(self, _e=None):
        chosen = self.var_lang.get()
        for code, name in self.controller.language_options():
            if name == chosen:
                self.controller.set_language(code)
                break
        self._apply_language()

    def _title_key(self):
        raise NotImplementedError

    def _refresh_mission(self):
        pass

    # ------ Drawing ------
    def _node_style(self, idx):
        return ("#E1F5FE", "#0288D1", "#01579B")

    def _draw_graph(self):
        if self.n == 0:
            return
        self.canvas.delete("all")
        self.canvas.update_idletasks()
        w = max(self.canvas.winfo_width(), 100)
        h = max(self.canvas.winfo_height(), 100)
        cx, cy = w / 2, h / 2
        r = min(w, h) * 0.36
        self.positions = circular_layout(self.n, cx, cy, r)

        node_r = self.NODE_R
        edge_set = set()
        if self.directed:
            edge_set = {(e[0], e[1]) for e in self.edges}

        for e in self.edges:
            if len(e) == 3:
                u, v, weight = e
            else:
                u, v = e
                weight = None
            x1, y1 = self.positions[u]
            x2, y2 = self.positions[v]
            dx, dy = x2 - x1, y2 - y1
            d = math.hypot(dx, dy) or 1
            ux, uy = dx / d, dy / d
            has_opposite = self.directed and (v, u) in edge_set
            if has_opposite:
                ox, oy = -uy, ux
                offset = 11
            else:
                ox, oy = 0.0, 0.0
                offset = 0
            sx = x1 + ux * node_r + ox * offset
            sy = y1 + uy * node_r + oy * offset
            ex = x2 - ux * node_r + ox * offset
            ey = y2 - uy * node_r + oy * offset
            if self.directed:
                self.canvas.create_line(sx, sy, ex, ey, arrow=tk.LAST, fill="#555", width=2)
            else:
                self.canvas.create_line(sx, sy, ex, ey, fill="#555", width=2)
            if weight is not None:
                mx = (sx + ex) / 2 + ox * 10
                my = (sy + ey) / 2 + oy * 10
                if weight < 0:
                    bg, fg = "#FFEBEE", "#C62828"
                else:
                    bg, fg = "#FFFDE7", "#333"
                self.canvas.create_rectangle(
                    mx - 14, my - 9, mx + 14, my + 9,
                    fill=bg, outline="#bbb",
                )
                self.canvas.create_text(
                    mx, my, text=str(weight),
                    font=("Arial", 10, "bold"), fill=fg,
                )

        for i, (x, y) in enumerate(self.positions):
            fill, outline, text_color = self._node_style(i)
            self.canvas.create_oval(
                x - node_r, y - node_r, x + node_r, y + node_r,
                fill=fill, outline=outline, width=2,
            )
            self.canvas.create_text(
                x, y, text=str(i + 1),
                font=("Arial", 12, "bold"), fill=text_color,
            )

    # ------ Lifecycle ------
    def new_exercise(self):
        self.answered = False
        self.stats_recorded = False
        self.entry.delete(0, tk.END)
        self.lbl_feedback.config(text="")
        self._generate()
        self._refresh_mission()
        self.entry.focus()
        self.after(50, self._draw_graph)

    def _generate(self):
        raise NotImplementedError

    def verify(self):
        raise NotImplementedError

    def _record(self, correct):
        if not self.stats_recorded:
            stats_tracker.record(self.stats_cat, correct)
            self.stats_recorded = True


# ============================================================
# Dijkstra screen
# ============================================================

class DijkstraScreen(_GraphScreenBase):
    def __init__(self, parent, controller, on_back):
        self.src = 0
        self.expected = []
        super().__init__(parent, controller, on_back, "dijkstra", "#2E7D32")

    def _title_key(self):
        return "dijkstra_title"

    def _refresh_mission(self):
        if self.n == 0:
            return
        others = [i + 1 for i in range(self.n) if i != self.src]
        self.lbl_mission.config(text=self.t(
            "dijkstra_mission",
            src=self.src + 1,
            nodes=", ".join(str(x) for x in others),
        ))

    def _generate(self):
        self.n = random.choice([4, 5, 5, 6])
        self.directed = True
        self.weighted = True
        for _ in range(60):
            edges = gen_weighted_digraph(self.n, density=0.4, w_min=1, w_max=9)
            self.edges = edges
            self.src = random.randint(0, self.n - 1)
            self.expected = dijkstra(self.n, edges, self.src)
            finite = [d for i, d in enumerate(self.expected) if i != self.src and d < math.inf]
            if finite:
                return

    def _node_style(self, idx):
        if idx == self.src:
            return ("#A5D6A7", "#1B5E20", "#1B5E20")
        return ("#E1F5FE", "#0288D1", "#01579B")

    def verify(self):
        if self.answered:
            return
        text = self.entry.get().strip()
        if not text:
            self.lbl_feedback.config(text=self.t("graph_empty"), fg="#FF9800")
            return
        expected_others = [self.expected[i] for i in range(self.n) if i != self.src]
        user = _parse_dist_list(text, len(expected_others))
        if user is None:
            self.lbl_feedback.config(text=self.t("graph_format_error"), fg="#FF9800")
            return
        correct = all(u == e for u, e in zip(user, expected_others))
        self.answered = True
        self._record(correct)
        if correct:
            self.lbl_feedback.config(text=self.t("graph_correct"), fg="#4CAF50")
        else:
            self.lbl_feedback.config(
                text=self.t("graph_wrong_full",
                            user=_format_dist_list(user),
                            correct=_format_dist_list(expected_others)),
                fg="#F44336",
            )


# ============================================================
# Bellman-Ford screen
# ============================================================

class BellmanScreen(_GraphScreenBase):
    def __init__(self, parent, controller, on_back):
        self.src = 0
        self.expected = []
        self.has_neg_cycle = False
        super().__init__(parent, controller, on_back, "bellman", "#F57C00")

    def _title_key(self):
        return "bellman_title"

    def _build_extra_buttons(self, row):
        self.btn_neg_cycle = tk.Button(
            row, command=self.declare_neg_cycle, bg="#C62828", fg="white",
            font=("Arial", 11, "bold"), padx=10,
        )
        self.btn_neg_cycle.pack(side=tk.LEFT, padx=5)

    def _apply_language_extra(self):
        if hasattr(self, "btn_neg_cycle"):
            self.btn_neg_cycle.config(text=self.t("bellman_neg_cycle_btn"))

    def _refresh_mission(self):
        if self.n == 0:
            return
        others = [i + 1 for i in range(self.n) if i != self.src]
        self.lbl_mission.config(text=self.t(
            "bellman_mission",
            src=self.src + 1,
            nodes=", ".join(str(x) for x in others),
        ))

    def _generate(self):
        self.n = random.choice([4, 4, 5])
        self.directed = True
        self.weighted = True
        want_neg_cycle = random.random() < 0.3
        last_dist, last_nc, last_edges, last_src = None, False, [], 0
        for _ in range(120):
            edges = gen_weighted_digraph(self.n, density=0.42, w_min=-3, w_max=8)
            if not any(w < 0 for _, _, w in edges):
                continue
            src = random.randint(0, self.n - 1)
            dist, has_nc = bellman_ford(self.n, edges, src)
            finite_others = [d for i, d in enumerate(dist) if i != src and d != math.inf]
            if not finite_others:
                continue
            last_dist, last_nc, last_edges, last_src = dist, has_nc, edges, src
            if want_neg_cycle == has_nc:
                break
        self.edges = last_edges
        self.src = last_src
        self.expected = last_dist if last_dist is not None else [math.inf] * self.n
        self.has_neg_cycle = last_nc

    def _node_style(self, idx):
        if idx == self.src:
            return ("#FFE0B2", "#E65100", "#E65100")
        return ("#E1F5FE", "#0288D1", "#01579B")

    def declare_neg_cycle(self):
        if self.answered:
            return
        self.answered = True
        if self.has_neg_cycle:
            self._record(True)
            self.lbl_feedback.config(text=self.t("bellman_neg_cycle_true"), fg="#4CAF50")
        else:
            self._record(False)
            expected_others = [self.expected[i] for i in range(self.n) if i != self.src]
            self.lbl_feedback.config(
                text=self.t("bellman_neg_cycle_false",
                            correct=_format_dist_list(expected_others)),
                fg="#F44336",
            )

    def verify(self):
        if self.answered:
            return
        text = self.entry.get().strip()
        if not text:
            self.lbl_feedback.config(text=self.t("graph_empty"), fg="#FF9800")
            return
        expected_others = [self.expected[i] for i in range(self.n) if i != self.src]
        user = _parse_dist_list(text, len(expected_others))
        if user is None:
            self.lbl_feedback.config(text=self.t("graph_format_error"), fg="#FF9800")
            return
        self.answered = True
        if self.has_neg_cycle:
            self._record(False)
            self.lbl_feedback.config(text=self.t("bellman_neg_cycle_missed"), fg="#F44336")
            return
        correct = all(u == e for u, e in zip(user, expected_others))
        self._record(correct)
        if correct:
            self.lbl_feedback.config(text=self.t("graph_correct"), fg="#4CAF50")
        else:
            self.lbl_feedback.config(
                text=self.t("graph_wrong_full",
                            user=_format_dist_list(user),
                            correct=_format_dist_list(expected_others)),
                fg="#F44336",
            )


# ============================================================
# Kosaraju screen
# ============================================================

class KosarajuScreen(_GraphScreenBase):
    def __init__(self, parent, controller, on_back):
        self.expected_sccs = []
        super().__init__(parent, controller, on_back, "kosaraju", "#6A1B9A")

    def _title_key(self):
        return "kosaraju_title"

    def _refresh_mission(self):
        self.lbl_mission.config(text=self.t("kosaraju_mission"))

    def _generate(self):
        self.n = random.choice([5, 6, 6, 7])
        self.directed = True
        self.weighted = False
        last_edges = None
        last_sccs = None
        for _ in range(60):
            edges = gen_unweighted_digraph(self.n, density=0.32)
            sccs = kosaraju(self.n, edges)
            last_edges, last_sccs = edges, sccs
            if 2 <= len(sccs) <= self.n - 1 and any(len(s) >= 2 for s in sccs):
                break
        self.edges = last_edges
        self.expected_sccs = [frozenset(s) for s in last_sccs]

    def verify(self):
        if self.answered:
            return
        text = self.entry.get().strip()
        if not text:
            self.lbl_feedback.config(text=self.t("graph_empty"), fg="#FF9800")
            return
        groups = _parse_scc_groups(text)
        if groups is None:
            self.lbl_feedback.config(text=self.t("graph_format_error"), fg="#FF9800")
            return
        user_sets = set(frozenset(x - 1 for x in g) for g in groups)
        correct_sets = set(self.expected_sccs)
        ok = user_sets == correct_sets
        self.answered = True
        self._record(ok)
        if ok:
            self.lbl_feedback.config(text=self.t("graph_correct"), fg="#4CAF50")
        else:
            self.lbl_feedback.config(
                text=self.t("graph_wrong_full",
                            user=_format_sccs(user_sets),
                            correct=_format_sccs(correct_sets)),
                fg="#F44336",
            )


# ============================================================
# Erdős number screen
# ============================================================

class ErdosScreen(_GraphScreenBase):
    def __init__(self, parent, controller, on_back):
        self.src = 0
        self.expected = []
        super().__init__(parent, controller, on_back, "erdos", "#00838F")

    def _title_key(self):
        return "erdos_title"

    def _refresh_mission(self):
        if self.n == 0:
            return
        others = [i + 1 for i in range(self.n) if i != self.src]
        self.lbl_mission.config(text=self.t(
            "erdos_mission",
            src=self.src + 1,
            nodes=", ".join(str(x) for x in others),
        ))

    def _generate(self):
        self.n = random.choice([5, 6, 7])
        self.directed = False
        self.weighted = False
        last_edges, last_src, last_dist = None, 0, None
        for _ in range(40):
            edges = gen_undirected(self.n, density=0.32)
            adj = [[] for _ in range(self.n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            src = random.randint(0, self.n - 1)
            dist = bfs_dist(self.n, adj, src)
            reachable = sum(1 for d in dist if d != math.inf)
            last_edges, last_src, last_dist = edges, src, dist
            if 2 <= reachable <= self.n:
                break
        self.edges = last_edges
        self.src = last_src
        self.expected = last_dist

    def _node_style(self, idx):
        if idx == self.src:
            return ("#B2DFDB", "#004D40", "#004D40")
        return ("#E1F5FE", "#0288D1", "#01579B")

    def verify(self):
        if self.answered:
            return
        text = self.entry.get().strip()
        if not text:
            self.lbl_feedback.config(text=self.t("graph_empty"), fg="#FF9800")
            return
        expected_others = [self.expected[i] for i in range(self.n) if i != self.src]
        user = _parse_dist_list(text, len(expected_others))
        if user is None:
            self.lbl_feedback.config(text=self.t("graph_format_error"), fg="#FF9800")
            return
        correct = all(u == e for u, e in zip(user, expected_others))
        self.answered = True
        self._record(correct)
        if correct:
            self.lbl_feedback.config(text=self.t("graph_correct"), fg="#4CAF50")
        else:
            self.lbl_feedback.config(
                text=self.t("graph_wrong_full",
                            user=_format_dist_list(user),
                            correct=_format_dist_list(expected_others)),
                fg="#F44336",
            )


# ============================================================
# Graph sub-menu
# ============================================================

class GraphMenuScreen(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root, bg="#f0f0f0")
        self.controller = controller
        self.sub_screen = None
        self._build_menu()

    def t(self, key, **fmt):
        return self.controller.t(key, **fmt)

    def _clear(self):
        for w in self.winfo_children():
            w.destroy()
        self.sub_screen = None

    def _build_menu(self):
        self._clear()

        top = tk.Frame(self, bg="#e0e0e0", pady=10, padx=12, relief=tk.RAISED, bd=2)
        top.pack(fill=tk.X, padx=10, pady=(10, 5))

        tk.Button(
            top, text=self.t("graph_back_menu"),
            command=self.controller.show_menu,
            bg="#757575", fg="white", font=("Arial", 10, "bold"), padx=10,
        ).pack(side=tk.LEFT)

        tk.Label(
            top, text=self.t("language"), bg="#e0e0e0",
            font=("Arial", 11, "bold"),
        ).pack(side=tk.LEFT, padx=(15, 0))
        lang_pairs = self.controller.language_options()
        current_name = next(name for code, name in lang_pairs if code == self.controller.lang)
        var_lang = tk.StringVar(value=current_name)
        cb = ttk.Combobox(
            top, textvariable=var_lang, width=14, state="readonly",
            values=[name for _c, name in lang_pairs],
        )
        cb.pack(side=tk.LEFT, padx=8)

        def _on_lang(_e=None):
            chosen = var_lang.get()
            for code, name in self.controller.language_options():
                if name == chosen:
                    self.controller.set_language(code)
                    self._build_menu()
                    return
        cb.bind("<<ComboboxSelected>>", _on_lang)

        tk.Label(
            self, text=self.t("graph_menu_title"),
            font=("Arial", 22, "bold"), bg="#f0f0f0", fg="#222",
        ).pack(pady=(24, 4))
        tk.Label(
            self, text=self.t("graph_menu_subtitle"),
            font=("Arial", 11, "italic"), bg="#f0f0f0", fg="#666",
        ).pack(pady=(0, 16))

        btn_frame = tk.Frame(self, bg="#f0f0f0")
        btn_frame.pack(pady=10)

        configs = [
            ("graph_dijkstra", "#2E7D32", DijkstraScreen),
            ("graph_bellman",  "#F57C00", BellmanScreen),
            ("graph_kosaraju", "#6A1B9A", KosarajuScreen),
            ("graph_erdos",    "#00838F", ErdosScreen),
        ]
        for key, color, screen_cls in configs:
            tk.Button(
                btn_frame, text=self.t(key),
                command=lambda c=screen_cls: self._show_exercise(c),
                bg=color, fg="white", font=("Arial", 12, "bold"),
                width=44, height=2, relief=tk.RAISED, bd=3,
                activebackground=color, cursor="hand2", justify="center",
            ).pack(pady=6)

    def _show_exercise(self, cls):
        self._clear()
        self.sub_screen = cls(self, self.controller, self._build_menu)
        self.sub_screen.pack(expand=True, fill=tk.BOTH)

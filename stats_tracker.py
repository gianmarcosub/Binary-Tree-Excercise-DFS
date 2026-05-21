import os


STATS_FILE = os.path.join(os.path.expanduser("~"), "Documents", "statistiche_algoritmi.txt")

CATEGORIES = ["dfs", "bfs", "rb", "async", "sort", "sort_row", "sort_table", "ai"]


STATS_TRANSLATIONS = {
    "it": {
        "stats_active": "📊 Modalità Statistiche attiva — Random Mix pesato",
        "stats_inactive": "Modalità Statistiche disattivata",
        "stats_create_btn": "📊 Crea file statistiche",
        "stats_view_btn": "📊 Vedi Statistiche",
        "stats_reset_btn": "🔄 Azzera",
        "stats_close_btn": "Chiudi",
        "stats_window_title": "Statistiche Algoritmi",
        "stats_path_label": "File: {path}",
        "stats_create_ok": "✅ File creato: {path}",
        "stats_create_err": "⚠ Errore creazione file: {err}",
        "stats_header_cat": "Categoria",
        "stats_header_right": "Giusti",
        "stats_header_wrong": "Sbagliati",
        "stats_header_pct": "% Errori",
        "stats_header_weight": "Peso Random",
        "stats_total_row": "TOTALE",
        "stats_no_data": "Nessun dato ancora registrato.",
        "stats_reset_confirm": "Azzerare tutte le statistiche?",
        "cat_dfs": "DFS",
        "cat_bfs": "BFS",
        "cat_rb": "Rosso-Nero",
        "cat_async": "Notazioni Asintotiche",
        "cat_sort": "Ordinamento (codice)",
        "cat_sort_row": "Tabella riga singola",
        "cat_sort_table": "Tabella completa",
        "cat_ai": "Codice AI (Gemini)",
    },
    "en": {
        "stats_active": "📊 Stats Mode active — weighted Random Mix",
        "stats_inactive": "Stats Mode disabled",
        "stats_create_btn": "📊 Create stats file",
        "stats_view_btn": "📊 View Statistics",
        "stats_reset_btn": "🔄 Reset",
        "stats_close_btn": "Close",
        "stats_window_title": "Algorithm Statistics",
        "stats_path_label": "File: {path}",
        "stats_create_ok": "✅ File created: {path}",
        "stats_create_err": "⚠ Could not create file: {err}",
        "stats_header_cat": "Category",
        "stats_header_right": "Correct",
        "stats_header_wrong": "Wrong",
        "stats_header_pct": "% Errors",
        "stats_header_weight": "Random Weight",
        "stats_total_row": "TOTAL",
        "stats_no_data": "No data recorded yet.",
        "stats_reset_confirm": "Reset all statistics?",
        "cat_dfs": "DFS",
        "cat_bfs": "BFS",
        "cat_rb": "Red-Black",
        "cat_async": "Asymptotic Notation",
        "cat_sort": "Sorting (code)",
        "cat_sort_row": "Single-row table",
        "cat_sort_table": "Full table",
        "cat_ai": "AI code (Gemini)",
    },
    "es": {
        "stats_active": "📊 Modo Estadísticas activo — Random Mix ponderado",
        "stats_inactive": "Modo Estadísticas desactivado",
        "stats_create_btn": "📊 Crear archivo de estadísticas",
        "stats_view_btn": "📊 Ver Estadísticas",
        "stats_reset_btn": "🔄 Restablecer",
        "stats_close_btn": "Cerrar",
        "stats_window_title": "Estadísticas de Algoritmos",
        "stats_path_label": "Archivo: {path}",
        "stats_create_ok": "✅ Archivo creado: {path}",
        "stats_create_err": "⚠ No se pudo crear el archivo: {err}",
        "stats_header_cat": "Categoría",
        "stats_header_right": "Correctas",
        "stats_header_wrong": "Erradas",
        "stats_header_pct": "% Errores",
        "stats_header_weight": "Peso Random",
        "stats_total_row": "TOTAL",
        "stats_no_data": "Aún no hay datos registrados.",
        "stats_reset_confirm": "¿Restablecer todas las estadísticas?",
        "cat_dfs": "DFS",
        "cat_bfs": "BFS",
        "cat_rb": "Rojo-Negro",
        "cat_async": "Notación Asintótica",
        "cat_sort": "Ordenamiento (código)",
        "cat_sort_row": "Tabla fila única",
        "cat_sort_table": "Tabla completa",
        "cat_ai": "Código IA (Gemini)",
    },
    "fr": {
        "stats_active": "📊 Mode Statistiques actif — Random Mix pondéré",
        "stats_inactive": "Mode Statistiques désactivé",
        "stats_create_btn": "📊 Créer le fichier de statistiques",
        "stats_view_btn": "📊 Voir les Statistiques",
        "stats_reset_btn": "🔄 Réinitialiser",
        "stats_close_btn": "Fermer",
        "stats_window_title": "Statistiques des Algorithmes",
        "stats_path_label": "Fichier: {path}",
        "stats_create_ok": "✅ Fichier créé: {path}",
        "stats_create_err": "⚠ Impossible de créer le fichier: {err}",
        "stats_header_cat": "Catégorie",
        "stats_header_right": "Justes",
        "stats_header_wrong": "Fausses",
        "stats_header_pct": "% Erreurs",
        "stats_header_weight": "Poids Random",
        "stats_total_row": "TOTAL",
        "stats_no_data": "Aucune donnée enregistrée.",
        "stats_reset_confirm": "Réinitialiser toutes les statistiques?",
        "cat_dfs": "DFS",
        "cat_bfs": "BFS",
        "cat_rb": "Rouge-Noir",
        "cat_async": "Notation Asymptotique",
        "cat_sort": "Tri (code)",
        "cat_sort_row": "Tableau une ligne",
        "cat_sort_table": "Tableau complet",
        "cat_ai": "Code IA (Gemini)",
    },
    "de": {
        "stats_active": "📊 Statistik-Modus aktiv — gewichtetes Random Mix",
        "stats_inactive": "Statistik-Modus deaktiviert",
        "stats_create_btn": "📊 Statistikdatei anlegen",
        "stats_view_btn": "📊 Statistiken anzeigen",
        "stats_reset_btn": "🔄 Zurücksetzen",
        "stats_close_btn": "Schließen",
        "stats_window_title": "Algorithmen-Statistiken",
        "stats_path_label": "Datei: {path}",
        "stats_create_ok": "✅ Datei angelegt: {path}",
        "stats_create_err": "⚠ Datei konnte nicht angelegt werden: {err}",
        "stats_header_cat": "Kategorie",
        "stats_header_right": "Richtig",
        "stats_header_wrong": "Falsch",
        "stats_header_pct": "% Fehler",
        "stats_header_weight": "Random-Gewicht",
        "stats_total_row": "GESAMT",
        "stats_no_data": "Noch keine Daten erfasst.",
        "stats_reset_confirm": "Alle Statistiken zurücksetzen?",
        "cat_dfs": "DFS",
        "cat_bfs": "BFS",
        "cat_rb": "Rot-Schwarz",
        "cat_async": "Asymptotische Notation",
        "cat_sort": "Sortierung (Code)",
        "cat_sort_row": "Tabelle Einzelzeile",
        "cat_sort_table": "Vollständige Tabelle",
        "cat_ai": "KI-Code (Gemini)",
    },
    "pt": {
        "stats_active": "📊 Modo Estatísticas ativo — Random Mix ponderado",
        "stats_inactive": "Modo Estatísticas desativado",
        "stats_create_btn": "📊 Criar arquivo de estatísticas",
        "stats_view_btn": "📊 Ver Estatísticas",
        "stats_reset_btn": "🔄 Zerar",
        "stats_close_btn": "Fechar",
        "stats_window_title": "Estatísticas de Algoritmos",
        "stats_path_label": "Arquivo: {path}",
        "stats_create_ok": "✅ Arquivo criado: {path}",
        "stats_create_err": "⚠ Não foi possível criar o arquivo: {err}",
        "stats_header_cat": "Categoria",
        "stats_header_right": "Certas",
        "stats_header_wrong": "Erradas",
        "stats_header_pct": "% Erros",
        "stats_header_weight": "Peso Random",
        "stats_total_row": "TOTAL",
        "stats_no_data": "Nenhum dado registrado.",
        "stats_reset_confirm": "Zerar todas as estatísticas?",
        "cat_dfs": "DFS",
        "cat_bfs": "BFS",
        "cat_rb": "Rubro-Negro",
        "cat_async": "Notação Assintótica",
        "cat_sort": "Ordenação (código)",
        "cat_sort_row": "Tabela linha única",
        "cat_sort_table": "Tabela completa",
        "cat_ai": "Código IA (Gemini)",
    },
}


def is_enabled():
    return os.path.isfile(STATS_FILE)


def _empty_stats():
    return {cat: {"right": 0, "wrong": 0} for cat in CATEGORIES}


def create_file():
    try:
        os.makedirs(os.path.dirname(STATS_FILE), exist_ok=True)
        if not os.path.isfile(STATS_FILE):
            save(_empty_stats())
        return True, None
    except OSError as e:
        return False, str(e)


def load():
    stats = _empty_stats()
    if not os.path.isfile(STATS_FILE):
        return stats
    try:
        with open(STATS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = [p.strip() for p in line.split(",")]
                if len(parts) != 3:
                    continue
                cat = parts[0]
                try:
                    right = int(parts[1])
                    wrong = int(parts[2])
                except ValueError:
                    continue
                if cat in stats:
                    stats[cat]["right"] = right
                    stats[cat]["wrong"] = wrong
    except OSError:
        pass
    return stats


def save(stats):
    with open(STATS_FILE, "w", encoding="utf-8") as f:
        f.write("# Statistiche Algoritmi\n")
        f.write("# Formato: categoria,giusti,sbagliati\n")
        for cat in CATEGORIES:
            d = stats.get(cat, {"right": 0, "wrong": 0})
            f.write(f"{cat},{d['right']},{d['wrong']}\n")


def record(category, correct):
    if not is_enabled():
        return
    if category not in CATEGORIES:
        return
    stats = load()
    if correct:
        stats[category]["right"] += 1
    else:
        stats[category]["wrong"] += 1
    try:
        save(stats)
    except OSError:
        pass


def reset():
    if not is_enabled():
        return
    try:
        save(_empty_stats())
    except OSError:
        pass


def weight_for(cat_data):
    total = cat_data["right"] + cat_data["wrong"]
    if total == 0:
        return 4.0
    error_rate = cat_data["wrong"] / total
    return 1.0 + 6.0 * error_rate


def weights(category_keys):
    if not is_enabled():
        return None
    stats = load()
    out = []
    for cat in category_keys:
        d = stats.get(cat, {"right": 0, "wrong": 0})
        out.append(weight_for(d))
    return out

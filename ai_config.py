import json
import os
import urllib.error
import urllib.request


CONFIG_FILE = os.path.join(
    os.path.expanduser("~"), "Documents", "algoritmi_ai_config.txt"
)

# Selectable Gemini models (label shown to the user -> API model id).
MODELS = [
    "gemini-2.5-flash",
    "gemini-2.5-pro",
    "gemini-2.0-flash",
    "gemini-1.5-flash",
    "gemini-1.5-pro",
]
DEFAULT_MODEL = "gemini-2.5-flash"

API_KEY_URL = "https://aistudio.google.com/app/apikey"


AI_TRANSLATIONS = {
    "it": {
        "menu_ai": "🤖 Genera Codice con AI\nIndovina l'algoritmo",
        "ai_title": "Genera Codice con AI",
        "ai_config_btn": "⚙ Configura AI (Gemini)",
        "ai_config_title": "Configurazione AI — Gemini",
        "ai_config_key_label": "Chiave API Gemini:",
        "ai_config_model_label": "Modello:",
        "ai_config_save": "💾 Salva",
        "ai_config_cancel": "Annulla",
        "ai_config_saved": "✅ Configurazione salvata.",
        "ai_config_key_hint": "Ottieni una chiave gratuita su: {url}",
        "ai_config_show_key": "Mostra chiave",
        "ai_not_configured": "⚠ Nessuna chiave API Gemini configurata.\nConfigura l'AI per usare questa modalità.",
        "ai_open_config": "⚙ Configura AI",
        "ai_generate": "✨ Genera nuovo codice",
        "ai_question": "Quale algoritmo ha generato l'AI?",
        "ai_pick": "Scegli la risposta cliccando una delle opzioni qui sotto:",
        "ai_generating": "⏳ Generazione del codice in corso...",
        "ai_error": "⚠ Errore: {err}",
        "ai_correct": "✅ ESATTO! L'algoritmo era {ans}.",
        "ai_wrong": "❌ Sbagliato. L'algoritmo corretto era {ans}.",
        "ai_model_label": "Modello: {model}",
    },
    "en": {
        "menu_ai": "🤖 Generate Code with AI\nGuess the algorithm",
        "ai_title": "Generate Code with AI",
        "ai_config_btn": "⚙ Configure AI (Gemini)",
        "ai_config_title": "AI Configuration — Gemini",
        "ai_config_key_label": "Gemini API key:",
        "ai_config_model_label": "Model:",
        "ai_config_save": "💾 Save",
        "ai_config_cancel": "Cancel",
        "ai_config_saved": "✅ Configuration saved.",
        "ai_config_key_hint": "Get a free key at: {url}",
        "ai_config_show_key": "Show key",
        "ai_not_configured": "⚠ No Gemini API key configured.\nConfigure the AI to use this mode.",
        "ai_open_config": "⚙ Configure AI",
        "ai_generate": "✨ Generate new code",
        "ai_question": "Which algorithm did the AI generate?",
        "ai_pick": "Pick your answer by clicking one of the options below:",
        "ai_generating": "⏳ Generating code...",
        "ai_error": "⚠ Error: {err}",
        "ai_correct": "✅ CORRECT! The algorithm was {ans}.",
        "ai_wrong": "❌ Wrong. The correct algorithm was {ans}.",
        "ai_model_label": "Model: {model}",
    },
    "es": {
        "menu_ai": "🤖 Generar Código con IA\nAdivina el algoritmo",
        "ai_title": "Generar Código con IA",
        "ai_config_btn": "⚙ Configurar IA (Gemini)",
        "ai_config_title": "Configuración IA — Gemini",
        "ai_config_key_label": "Clave API de Gemini:",
        "ai_config_model_label": "Modelo:",
        "ai_config_save": "💾 Guardar",
        "ai_config_cancel": "Cancelar",
        "ai_config_saved": "✅ Configuración guardada.",
        "ai_config_key_hint": "Consigue una clave gratis en: {url}",
        "ai_config_show_key": "Mostrar clave",
        "ai_not_configured": "⚠ No hay clave API de Gemini configurada.\nConfigura la IA para usar este modo.",
        "ai_open_config": "⚙ Configurar IA",
        "ai_generate": "✨ Generar nuevo código",
        "ai_question": "¿Qué algoritmo generó la IA?",
        "ai_pick": "Elige tu respuesta haciendo clic en una de las opciones:",
        "ai_generating": "⏳ Generando código...",
        "ai_error": "⚠ Error: {err}",
        "ai_correct": "✅ ¡CORRECTO! El algoritmo era {ans}.",
        "ai_wrong": "❌ Incorrecto. El algoritmo correcto era {ans}.",
        "ai_model_label": "Modelo: {model}",
    },
    "fr": {
        "menu_ai": "🤖 Générer du Code avec l'IA\nDevine l'algorithme",
        "ai_title": "Générer du Code avec l'IA",
        "ai_config_btn": "⚙ Configurer l'IA (Gemini)",
        "ai_config_title": "Configuration IA — Gemini",
        "ai_config_key_label": "Clé API Gemini :",
        "ai_config_model_label": "Modèle :",
        "ai_config_save": "💾 Enregistrer",
        "ai_config_cancel": "Annuler",
        "ai_config_saved": "✅ Configuration enregistrée.",
        "ai_config_key_hint": "Obtenez une clé gratuite sur : {url}",
        "ai_config_show_key": "Afficher la clé",
        "ai_not_configured": "⚠ Aucune clé API Gemini configurée.\nConfigurez l'IA pour utiliser ce mode.",
        "ai_open_config": "⚙ Configurer l'IA",
        "ai_generate": "✨ Générer un nouveau code",
        "ai_question": "Quel algorithme l'IA a-t-elle généré ?",
        "ai_pick": "Choisissez votre réponse en cliquant sur une option :",
        "ai_generating": "⏳ Génération du code...",
        "ai_error": "⚠ Erreur : {err}",
        "ai_correct": "✅ CORRECT ! L'algorithme était {ans}.",
        "ai_wrong": "❌ Faux. L'algorithme correct était {ans}.",
        "ai_model_label": "Modèle : {model}",
    },
    "de": {
        "menu_ai": "🤖 Code mit KI generieren\nErrate den Algorithmus",
        "ai_title": "Code mit KI generieren",
        "ai_config_btn": "⚙ KI konfigurieren (Gemini)",
        "ai_config_title": "KI-Konfiguration — Gemini",
        "ai_config_key_label": "Gemini API-Schlüssel:",
        "ai_config_model_label": "Modell:",
        "ai_config_save": "💾 Speichern",
        "ai_config_cancel": "Abbrechen",
        "ai_config_saved": "✅ Konfiguration gespeichert.",
        "ai_config_key_hint": "Hol dir einen kostenlosen Schlüssel: {url}",
        "ai_config_show_key": "Schlüssel anzeigen",
        "ai_not_configured": "⚠ Kein Gemini API-Schlüssel konfiguriert.\nKonfiguriere die KI, um diesen Modus zu nutzen.",
        "ai_open_config": "⚙ KI konfigurieren",
        "ai_generate": "✨ Neuen Code generieren",
        "ai_question": "Welchen Algorithmus hat die KI generiert?",
        "ai_pick": "Wähle deine Antwort durch Klick auf eine Option:",
        "ai_generating": "⏳ Code wird generiert...",
        "ai_error": "⚠ Fehler: {err}",
        "ai_correct": "✅ RICHTIG! Der Algorithmus war {ans}.",
        "ai_wrong": "❌ Falsch. Der korrekte Algorithmus war {ans}.",
        "ai_model_label": "Modell: {model}",
    },
    "pt": {
        "menu_ai": "🤖 Gerar Código com IA\nAdivinhe o algoritmo",
        "ai_title": "Gerar Código com IA",
        "ai_config_btn": "⚙ Configurar IA (Gemini)",
        "ai_config_title": "Configuração IA — Gemini",
        "ai_config_key_label": "Chave API Gemini:",
        "ai_config_model_label": "Modelo:",
        "ai_config_save": "💾 Salvar",
        "ai_config_cancel": "Cancelar",
        "ai_config_saved": "✅ Configuração salva.",
        "ai_config_key_hint": "Obtenha uma chave grátis em: {url}",
        "ai_config_show_key": "Mostrar chave",
        "ai_not_configured": "⚠ Nenhuma chave API Gemini configurada.\nConfigure a IA para usar este modo.",
        "ai_open_config": "⚙ Configurar IA",
        "ai_generate": "✨ Gerar novo código",
        "ai_question": "Qual algoritmo a IA gerou?",
        "ai_pick": "Escolha sua resposta clicando em uma das opções:",
        "ai_generating": "⏳ Gerando código...",
        "ai_error": "⚠ Erro: {err}",
        "ai_correct": "✅ CORRETO! O algoritmo era {ans}.",
        "ai_wrong": "❌ Errado. O algoritmo correto era {ans}.",
        "ai_model_label": "Modelo: {model}",
    },
}


def load():
    """Return {'api_key': str, 'model': str}. Missing file -> empty key."""
    cfg = {"api_key": "", "model": DEFAULT_MODEL}
    if not os.path.isfile(CONFIG_FILE):
        return cfg
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                key = key.strip()
                value = value.strip()
                if key in cfg:
                    cfg[key] = value
    except OSError:
        pass
    if cfg["model"] not in MODELS:
        cfg["model"] = DEFAULT_MODEL
    return cfg


def save(api_key, model):
    if model not in MODELS:
        model = DEFAULT_MODEL
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        f.write("# Configurazione AI Gemini\n")
        f.write("# Formato: chiave=valore\n")
        f.write(f"api_key={api_key.strip()}\n")
        f.write(f"model={model}\n")


def is_configured():
    return bool(load()["api_key"])


def generate_code(prompt, timeout=45):
    """Call the Gemini REST API and return the generated text.

    Raises RuntimeError with a human-readable message on failure.
    """
    cfg = load()
    api_key = cfg["api_key"]
    model = cfg["model"]
    if not api_key:
        raise RuntimeError("API key not configured")

    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent?key={api_key}"
    )
    payload = json.dumps(
        {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.7},
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        url, data=payload, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        try:
            err_body = json.loads(e.read().decode("utf-8"))
            msg = err_body.get("error", {}).get("message", str(e))
        except Exception:
            msg = f"HTTP {e.code}"
        raise RuntimeError(msg)
    except urllib.error.URLError as e:
        raise RuntimeError(f"Network error: {e.reason}")
    except Exception as e:  # noqa: BLE001
        raise RuntimeError(str(e))

    try:
        parts = data["candidates"][0]["content"]["parts"]
        text = "".join(p.get("text", "") for p in parts)
    except (KeyError, IndexError):
        raise RuntimeError("Unexpected API response")
    return text.strip()

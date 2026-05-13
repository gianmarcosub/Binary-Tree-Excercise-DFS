import tkinter as tk
from tkinter import ttk
import random

from sorting_exercise import SortingScreen, SORT_TRANSLATIONS
from bfs_exercise import BFSScreen, BFS_TRANSLATIONS
from sorting_table_exercise import SortingTableScreen, SORT_TABLE_TRANSLATIONS
from sort_table_row_exercise import SORT_TABLE_ROW_TRANSLATIONS
from random_mix_exercise import RandomMixScreen, RANDOM_MIX_TRANSLATIONS
import stats_tracker


TRANSLATIONS = {
    "it": {
        "lang_name": "Italiano",
        "app_title": "Esercitazioni Algoritmi & Strutture Dati",
        "language": "Lingua:",
        "back": "← Menu",
        # Menu
        "menu_title": "Scegli il tipo di esercitazione",
        "menu_subtitle": "Seleziona una modalità per iniziare",
        "menu_dfs": "Visite DFS\nPre-order · In-order · Post-order",
        "menu_rb": "Alberi Rosso-Nero\nRiconoscimento di validità",
        "menu_async": "Notazioni Asintotiche\nAnalisi della complessità",
        # DFS
        "title": "Simulatore DFS - Alberi Binari",
        "depth": "Profondità max:",
        "balanced": "Albero bilanciato",
        "show_hint": "Mostra suggerimento ordine",
        "generate": "🔄 Nuovo Albero",
        "zoom_in": "🔍+",
        "zoom_out": "🔍−",
        "zoom_reset": "1:1",
        "fit": "Adatta",
        "your_sequence": "La tua sequenza:",
        "verify": "Verifica",
        "mission_hint": "Missione: scrivi la sequenza di una visita {name} ({hint})",
        "mission_plain": "Missione: scrivi la sequenza di una visita {name}",
        "preorder": "PRE-ORDER",
        "inorder": "IN-ORDER",
        "postorder": "POST-ORDER",
        "preorder_hint": "Radice → Sinistra → Destra",
        "inorder_hint": "Sinistra → Radice → Destra",
        "postorder_hint": "Sinistra → Destra → Radice",
        "empty": "⚠ Inserisci dei numeri prima di verificare.",
        "correct": "✅ ESATTO! Ottimo lavoro.",
        "wrong": "❌ Sbagliato.\nLa tua: {user}\nCorretta: {correct}",
        "format_error": "⚠ Formato non valido. Usa solo numeri separati da spazi o virgole.",
        "nodes": "Nodi: {n}",
        # Red-Black
        "rb_title": "Alberi Rosso-Nero",
        "rb_question": "L'albero qui sopra è un albero rosso-nero VALIDO?",
        "rb_yes": "✅ Sì, è valido",
        "rb_no": "❌ No, non è valido",
        "rb_new": "🔄 Nuovo Albero",
        "rb_correct_valid": "✅ ESATTO! È un albero rosso-nero valido.",
        "rb_correct_invalid": "✅ ESATTO! Non è valido perché {reason}.",
        "rb_wrong_was_valid": "❌ Sbagliato. In realtà l'albero ERA un rosso-nero valido.",
        "rb_wrong_was_invalid": "❌ Sbagliato. L'albero NON era valido perché {reason}.",
        "rb_reason_root": "la radice deve essere NERA",
        "rb_reason_red_red": "un nodo ROSSO ha un figlio ROSSO",
        "rb_reason_bh": "i cammini hanno altezze nere differenti",
        "rb_rules_title": "Proprietà di un albero rosso-nero:",
        "rb_rule_1": "1) Ogni nodo è rosso o nero.",
        "rb_rule_2": "2) La radice è nera.",
        "rb_rule_3": "3) Le foglie NIL (quadratini neri) sono nere.",
        "rb_rule_4": "4) Un nodo rosso non può avere figli rossi.",
        "rb_rule_5": "5) Ogni cammino da un nodo alle foglie NIL contiene lo stesso numero di nodi neri.",
        # Asymptotic
        "async_title": "Notazioni Asintotiche",
        "async_question": "Qual è la complessità temporale del seguente algoritmo?",
        "async_new": "🔄 Nuovo Esercizio",
        "async_pick": "Scegli la risposta cliccando una delle opzioni qui sotto:",
        "async_correct": "✅ ESATTO! La complessità è {ans}.\n{explain}",
        "async_wrong": "❌ Sbagliato. La risposta corretta è {ans}.\n{explain}",
        "expl_const": "Operazione costante: non dipende dalla dimensione dell'input.",
        "expl_loop": "Un singolo ciclo che scorre l'input una volta.",
        "expl_nested": "Due cicli annidati su n elementi: n × n.",
        "expl_binsearch": "Ad ogni passo lo spazio di ricerca si dimezza.",
        "expl_fib": "Ricorsione binaria senza memoizzazione: 2 chiamate ad ogni livello.",
        "expl_mergesort": "Ricorsione che dimezza l'input + merge lineare.",
        "expl_triple": "Tre cicli annidati su n elementi: n × n × n.",
        "expl_logn": "L'indice raddoppia ad ogni iterazione (log₂ n passi).",
        "expl_nlogn": "Un ciclo esterno O(n) con un ciclo interno O(log n).",
        "expl_harmonic": "La somma 1 + 1/2 + 1/3 + ... + 1/n è O(log n), ma il ciclo esterno è O(n).",
        "expl_sumi": "Il ciclo interno fa i iterazioni: 1+2+...+n = n(n+1)/2.",
    },
    "en": {
        "lang_name": "English",
        "app_title": "Algorithms & Data Structures Practice",
        "language": "Language:",
        "back": "← Menu",
        "menu_title": "Choose an exercise type",
        "menu_subtitle": "Select a mode to start",
        "menu_dfs": "DFS Traversals\nPre-order · In-order · Post-order",
        "menu_rb": "Red-Black Trees\nValidity recognition",
        "menu_async": "Asymptotic Notation\nComplexity analysis",
        "title": "DFS Simulator - Binary Trees",
        "depth": "Max depth:",
        "balanced": "Balanced tree",
        "show_hint": "Show order hint",
        "generate": "🔄 New Tree",
        "zoom_in": "🔍+",
        "zoom_out": "🔍−",
        "zoom_reset": "1:1",
        "fit": "Fit",
        "your_sequence": "Your sequence:",
        "verify": "Check",
        "mission_hint": "Mission: write the sequence of a {name} traversal ({hint})",
        "mission_plain": "Mission: write the sequence of a {name} traversal",
        "preorder": "PRE-ORDER",
        "inorder": "IN-ORDER",
        "postorder": "POST-ORDER",
        "preorder_hint": "Root → Left → Right",
        "inorder_hint": "Left → Root → Right",
        "postorder_hint": "Left → Right → Root",
        "empty": "⚠ Enter some numbers before checking.",
        "correct": "✅ CORRECT! Well done.",
        "wrong": "❌ Wrong.\nYours: {user}\nCorrect: {correct}",
        "format_error": "⚠ Invalid format. Use numbers separated by spaces or commas only.",
        "nodes": "Nodes: {n}",
        "rb_title": "Red-Black Trees",
        "rb_question": "Is the tree above a VALID red-black tree?",
        "rb_yes": "✅ Yes, valid",
        "rb_no": "❌ No, invalid",
        "rb_new": "🔄 New Tree",
        "rb_correct_valid": "✅ CORRECT! It is a valid red-black tree.",
        "rb_correct_invalid": "✅ CORRECT! It is invalid because {reason}.",
        "rb_wrong_was_valid": "❌ Wrong. The tree WAS a valid red-black tree.",
        "rb_wrong_was_invalid": "❌ Wrong. The tree was NOT valid because {reason}.",
        "rb_reason_root": "the root must be BLACK",
        "rb_reason_red_red": "a RED node has a RED child",
        "rb_reason_bh": "paths have different black heights",
        "rb_rules_title": "Red-black tree properties:",
        "rb_rule_1": "1) Every node is either red or black.",
        "rb_rule_2": "2) The root is black.",
        "rb_rule_3": "3) NIL leaves (small black squares) are black.",
        "rb_rule_4": "4) A red node cannot have red children.",
        "rb_rule_5": "5) Every path from a node to NIL leaves contains the same number of black nodes.",
        "async_title": "Asymptotic Notation",
        "async_question": "What is the time complexity of the following algorithm?",
        "async_new": "🔄 New Exercise",
        "async_pick": "Pick your answer by clicking one of the options below:",
        "async_correct": "✅ CORRECT! Complexity is {ans}.\n{explain}",
        "async_wrong": "❌ Wrong. The correct answer is {ans}.\n{explain}",
        "expl_const": "Constant operation: doesn't depend on input size.",
        "expl_loop": "A single loop scanning the input once.",
        "expl_nested": "Two nested loops over n elements: n × n.",
        "expl_binsearch": "At each step the search space is halved.",
        "expl_fib": "Binary recursion without memoization: 2 calls per level.",
        "expl_mergesort": "Recursion halving the input + linear merge.",
        "expl_triple": "Three nested loops over n elements: n × n × n.",
        "expl_logn": "The index doubles each iteration (log₂ n steps).",
        "expl_nlogn": "Outer O(n) loop with an inner O(log n) loop.",
        "expl_harmonic": "The sum 1 + 1/2 + ... + 1/n is O(log n), but the outer loop is O(n).",
        "expl_sumi": "The inner loop runs i times: 1+2+...+n = n(n+1)/2.",
    },
    "es": {
        "lang_name": "Español",
        "app_title": "Ejercicios de Algoritmos y Estructuras",
        "language": "Idioma:",
        "back": "← Menú",
        "menu_title": "Elige el tipo de ejercicio",
        "menu_subtitle": "Selecciona un modo para empezar",
        "menu_dfs": "Recorridos DFS\nPre-orden · In-orden · Post-orden",
        "menu_rb": "Árboles Rojo-Negro\nReconocimiento de validez",
        "menu_async": "Notación Asintótica\nAnálisis de complejidad",
        "title": "Simulador DFS - Árboles Binarios",
        "depth": "Profundidad máx:",
        "balanced": "Árbol equilibrado",
        "show_hint": "Mostrar pista del orden",
        "generate": "🔄 Nuevo Árbol",
        "zoom_in": "🔍+",
        "zoom_out": "🔍−",
        "zoom_reset": "1:1",
        "fit": "Ajustar",
        "your_sequence": "Tu secuencia:",
        "verify": "Comprobar",
        "mission_hint": "Misión: escribe la secuencia de un recorrido {name} ({hint})",
        "mission_plain": "Misión: escribe la secuencia de un recorrido {name}",
        "preorder": "PRE-ORDEN",
        "inorder": "IN-ORDEN",
        "postorder": "POST-ORDEN",
        "preorder_hint": "Raíz → Izquierda → Derecha",
        "inorder_hint": "Izquierda → Raíz → Derecha",
        "postorder_hint": "Izquierda → Derecha → Raíz",
        "empty": "⚠ Introduce números antes de comprobar.",
        "correct": "✅ ¡CORRECTO! Buen trabajo.",
        "wrong": "❌ Incorrecto.\nTuya: {user}\nCorrecta: {correct}",
        "format_error": "⚠ Formato no válido. Solo números separados por espacios o comas.",
        "nodes": "Nodos: {n}",
        "rb_title": "Árboles Rojo-Negro",
        "rb_question": "¿Es el árbol anterior un árbol rojo-negro VÁLIDO?",
        "rb_yes": "✅ Sí, válido",
        "rb_no": "❌ No, inválido",
        "rb_new": "🔄 Nuevo Árbol",
        "rb_correct_valid": "✅ ¡CORRECTO! Es un árbol rojo-negro válido.",
        "rb_correct_invalid": "✅ ¡CORRECTO! No es válido porque {reason}.",
        "rb_wrong_was_valid": "❌ Incorrecto. El árbol SÍ era un rojo-negro válido.",
        "rb_wrong_was_invalid": "❌ Incorrecto. El árbol NO era válido porque {reason}.",
        "rb_reason_root": "la raíz debe ser NEGRA",
        "rb_reason_red_red": "un nodo ROJO tiene un hijo ROJO",
        "rb_reason_bh": "los caminos tienen alturas negras distintas",
        "rb_rules_title": "Propiedades de un árbol rojo-negro:",
        "rb_rule_1": "1) Cada nodo es rojo o negro.",
        "rb_rule_2": "2) La raíz es negra.",
        "rb_rule_3": "3) Las hojas NIL (cuadrados negros) son negras.",
        "rb_rule_4": "4) Un nodo rojo no puede tener hijos rojos.",
        "rb_rule_5": "5) Cada camino de un nodo a las hojas NIL contiene el mismo número de nodos negros.",
        "async_title": "Notación Asintótica",
        "async_question": "¿Cuál es la complejidad temporal del siguiente algoritmo?",
        "async_new": "🔄 Nuevo Ejercicio",
        "async_pick": "Elige tu respuesta haciendo clic en una de las opciones:",
        "async_correct": "✅ ¡CORRECTO! La complejidad es {ans}.\n{explain}",
        "async_wrong": "❌ Incorrecto. La respuesta correcta es {ans}.\n{explain}",
        "expl_const": "Operación constante: no depende del tamaño de la entrada.",
        "expl_loop": "Un único bucle que recorre la entrada una vez.",
        "expl_nested": "Dos bucles anidados sobre n elementos: n × n.",
        "expl_binsearch": "En cada paso el espacio de búsqueda se reduce a la mitad.",
        "expl_fib": "Recursión binaria sin memoización: 2 llamadas por nivel.",
        "expl_mergesort": "Recursión que parte por la mitad + fusión lineal.",
        "expl_triple": "Tres bucles anidados sobre n elementos: n × n × n.",
        "expl_logn": "El índice se duplica en cada iteración (log₂ n pasos).",
        "expl_nlogn": "Bucle externo O(n) con bucle interno O(log n).",
        "expl_harmonic": "La suma 1 + 1/2 + ... + 1/n es O(log n), pero el bucle externo es O(n).",
        "expl_sumi": "El bucle interno corre i veces: 1+2+...+n = n(n+1)/2.",
    },
    "fr": {
        "lang_name": "Français",
        "app_title": "Exercices d'Algorithmes et Structures",
        "language": "Langue:",
        "back": "← Menu",
        "menu_title": "Choisissez le type d'exercice",
        "menu_subtitle": "Sélectionnez un mode pour commencer",
        "menu_dfs": "Parcours DFS\nPré-ordre · In-ordre · Post-ordre",
        "menu_rb": "Arbres Rouge-Noir\nReconnaissance de validité",
        "menu_async": "Notation Asymptotique\nAnalyse de complexité",
        "title": "Simulateur DFS - Arbres Binaires",
        "depth": "Profondeur max:",
        "balanced": "Arbre équilibré",
        "show_hint": "Afficher l'indice d'ordre",
        "generate": "🔄 Nouvel Arbre",
        "zoom_in": "🔍+",
        "zoom_out": "🔍−",
        "zoom_reset": "1:1",
        "fit": "Ajuster",
        "your_sequence": "Votre séquence:",
        "verify": "Vérifier",
        "mission_hint": "Mission: écris la séquence d'un parcours {name} ({hint})",
        "mission_plain": "Mission: écris la séquence d'un parcours {name}",
        "preorder": "PRÉ-ORDRE",
        "inorder": "IN-ORDRE",
        "postorder": "POST-ORDRE",
        "preorder_hint": "Racine → Gauche → Droite",
        "inorder_hint": "Gauche → Racine → Droite",
        "postorder_hint": "Gauche → Droite → Racine",
        "empty": "⚠ Entre des nombres avant de vérifier.",
        "correct": "✅ CORRECT! Bien joué.",
        "wrong": "❌ Faux.\nLa tienne: {user}\nCorrecte: {correct}",
        "format_error": "⚠ Format invalide. Uniquement des nombres séparés par espaces ou virgules.",
        "nodes": "Nœuds: {n}",
        "rb_title": "Arbres Rouge-Noir",
        "rb_question": "L'arbre ci-dessus est-il un arbre rouge-noir VALIDE?",
        "rb_yes": "✅ Oui, valide",
        "rb_no": "❌ Non, invalide",
        "rb_new": "🔄 Nouvel Arbre",
        "rb_correct_valid": "✅ CORRECT! C'est un arbre rouge-noir valide.",
        "rb_correct_invalid": "✅ CORRECT! Il n'est pas valide car {reason}.",
        "rb_wrong_was_valid": "❌ Faux. L'arbre ÉTAIT un rouge-noir valide.",
        "rb_wrong_was_invalid": "❌ Faux. L'arbre N'était PAS valide car {reason}.",
        "rb_reason_root": "la racine doit être NOIRE",
        "rb_reason_red_red": "un nœud ROUGE a un enfant ROUGE",
        "rb_reason_bh": "les chemins ont des hauteurs noires différentes",
        "rb_rules_title": "Propriétés d'un arbre rouge-noir:",
        "rb_rule_1": "1) Chaque nœud est rouge ou noir.",
        "rb_rule_2": "2) La racine est noire.",
        "rb_rule_3": "3) Les feuilles NIL (carrés noirs) sont noires.",
        "rb_rule_4": "4) Un nœud rouge ne peut pas avoir d'enfants rouges.",
        "rb_rule_5": "5) Chaque chemin d'un nœud aux feuilles NIL contient le même nombre de nœuds noirs.",
        "async_title": "Notation Asymptotique",
        "async_question": "Quelle est la complexité temporelle de l'algorithme suivant?",
        "async_new": "🔄 Nouvel Exercice",
        "async_pick": "Choisis ta réponse en cliquant sur l'une des options:",
        "async_correct": "✅ CORRECT! La complexité est {ans}.\n{explain}",
        "async_wrong": "❌ Faux. La bonne réponse est {ans}.\n{explain}",
        "expl_const": "Opération constante: indépendante de la taille de l'entrée.",
        "expl_loop": "Une seule boucle qui parcourt l'entrée une fois.",
        "expl_nested": "Deux boucles imbriquées sur n éléments: n × n.",
        "expl_binsearch": "À chaque étape l'espace de recherche est divisé par deux.",
        "expl_fib": "Récursion binaire sans mémoïsation: 2 appels par niveau.",
        "expl_mergesort": "Récursion qui divise par deux + fusion linéaire.",
        "expl_triple": "Trois boucles imbriquées sur n éléments: n × n × n.",
        "expl_logn": "L'index double à chaque itération (log₂ n étapes).",
        "expl_nlogn": "Boucle externe O(n) avec une boucle interne O(log n).",
        "expl_harmonic": "La somme 1 + 1/2 + ... + 1/n est O(log n), mais la boucle externe est O(n).",
        "expl_sumi": "La boucle interne fait i itérations: 1+2+...+n = n(n+1)/2.",
    },
    "de": {
        "lang_name": "Deutsch",
        "app_title": "Übungen zu Algorithmen & Datenstrukturen",
        "language": "Sprache:",
        "back": "← Menü",
        "menu_title": "Wähle eine Übungsart",
        "menu_subtitle": "Wähle einen Modus zum Starten",
        "menu_dfs": "DFS-Traversierungen\nPre-order · In-order · Post-order",
        "menu_rb": "Rot-Schwarz-Bäume\nGültigkeitserkennung",
        "menu_async": "Asymptotische Notation\nKomplexitätsanalyse",
        "title": "DFS-Simulator - Binärbäume",
        "depth": "Max. Tiefe:",
        "balanced": "Ausgeglichener Baum",
        "show_hint": "Reihenfolge-Hinweis zeigen",
        "generate": "🔄 Neuer Baum",
        "zoom_in": "🔍+",
        "zoom_out": "🔍−",
        "zoom_reset": "1:1",
        "fit": "Anpassen",
        "your_sequence": "Deine Reihenfolge:",
        "verify": "Prüfen",
        "mission_hint": "Aufgabe: Schreibe die Reihenfolge einer {name}-Traversierung ({hint})",
        "mission_plain": "Aufgabe: Schreibe die Reihenfolge einer {name}-Traversierung",
        "preorder": "PRE-ORDER",
        "inorder": "IN-ORDER",
        "postorder": "POST-ORDER",
        "preorder_hint": "Wurzel → Links → Rechts",
        "inorder_hint": "Links → Wurzel → Rechts",
        "postorder_hint": "Links → Rechts → Wurzel",
        "empty": "⚠ Gib Zahlen ein, bevor du prüfst.",
        "correct": "✅ RICHTIG! Gut gemacht.",
        "wrong": "❌ Falsch.\nDeine: {user}\nRichtig: {correct}",
        "format_error": "⚠ Ungültiges Format. Nur Zahlen, getrennt durch Leerzeichen oder Kommas.",
        "nodes": "Knoten: {n}",
        "rb_title": "Rot-Schwarz-Bäume",
        "rb_question": "Ist der Baum oben ein GÜLTIGER Rot-Schwarz-Baum?",
        "rb_yes": "✅ Ja, gültig",
        "rb_no": "❌ Nein, ungültig",
        "rb_new": "🔄 Neuer Baum",
        "rb_correct_valid": "✅ RICHTIG! Es ist ein gültiger Rot-Schwarz-Baum.",
        "rb_correct_invalid": "✅ RICHTIG! Er ist ungültig weil {reason}.",
        "rb_wrong_was_valid": "❌ Falsch. Der Baum WAR ein gültiger Rot-Schwarz-Baum.",
        "rb_wrong_was_invalid": "❌ Falsch. Der Baum war NICHT gültig weil {reason}.",
        "rb_reason_root": "die Wurzel muss SCHWARZ sein",
        "rb_reason_red_red": "ein ROTER Knoten hat ein ROTES Kind",
        "rb_reason_bh": "die Pfade haben unterschiedliche Schwarzhöhen",
        "rb_rules_title": "Eigenschaften eines Rot-Schwarz-Baums:",
        "rb_rule_1": "1) Jeder Knoten ist rot oder schwarz.",
        "rb_rule_2": "2) Die Wurzel ist schwarz.",
        "rb_rule_3": "3) NIL-Blätter (schwarze Quadrate) sind schwarz.",
        "rb_rule_4": "4) Ein roter Knoten darf keine roten Kinder haben.",
        "rb_rule_5": "5) Jeder Pfad von einem Knoten zu NIL-Blättern enthält dieselbe Anzahl schwarzer Knoten.",
        "async_title": "Asymptotische Notation",
        "async_question": "Was ist die Zeitkomplexität des folgenden Algorithmus?",
        "async_new": "🔄 Neue Aufgabe",
        "async_pick": "Wähle deine Antwort durch Klick auf eine der Optionen:",
        "async_correct": "✅ RICHTIG! Komplexität ist {ans}.\n{explain}",
        "async_wrong": "❌ Falsch. Die richtige Antwort ist {ans}.\n{explain}",
        "expl_const": "Konstante Operation: unabhängig von der Eingabegröße.",
        "expl_loop": "Eine einzelne Schleife, die die Eingabe einmal durchläuft.",
        "expl_nested": "Zwei verschachtelte Schleifen über n Elemente: n × n.",
        "expl_binsearch": "Bei jedem Schritt wird der Suchraum halbiert.",
        "expl_fib": "Binäre Rekursion ohne Memoization: 2 Aufrufe pro Ebene.",
        "expl_mergesort": "Rekursion mit Halbierung + lineares Mischen.",
        "expl_triple": "Drei verschachtelte Schleifen über n Elemente: n × n × n.",
        "expl_logn": "Der Index verdoppelt sich pro Iteration (log₂ n Schritte).",
        "expl_nlogn": "Äußere O(n)-Schleife mit innerer O(log n)-Schleife.",
        "expl_harmonic": "Die Summe 1 + 1/2 + ... + 1/n ist O(log n), aber die äußere Schleife ist O(n).",
        "expl_sumi": "Die innere Schleife läuft i Mal: 1+2+...+n = n(n+1)/2.",
    },
    "pt": {
        "lang_name": "Português",
        "app_title": "Exercícios de Algoritmos e Estruturas",
        "language": "Idioma:",
        "back": "← Menu",
        "menu_title": "Escolha o tipo de exercício",
        "menu_subtitle": "Selecione um modo para começar",
        "menu_dfs": "Percursos DFS\nPré-ordem · Em-ordem · Pós-ordem",
        "menu_rb": "Árvores Rubro-Negras\nReconhecimento de validade",
        "menu_async": "Notação Assintótica\nAnálise de complexidade",
        "title": "Simulador DFS - Árvores Binárias",
        "depth": "Profundidade máx:",
        "balanced": "Árvore balanceada",
        "show_hint": "Mostrar dica da ordem",
        "generate": "🔄 Nova Árvore",
        "zoom_in": "🔍+",
        "zoom_out": "🔍−",
        "zoom_reset": "1:1",
        "fit": "Ajustar",
        "your_sequence": "Sua sequência:",
        "verify": "Verificar",
        "mission_hint": "Missão: escreva a sequência de um percurso {name} ({hint})",
        "mission_plain": "Missão: escreva a sequência de um percurso {name}",
        "preorder": "PRÉ-ORDEM",
        "inorder": "EM-ORDEM",
        "postorder": "PÓS-ORDEM",
        "preorder_hint": "Raiz → Esquerda → Direita",
        "inorder_hint": "Esquerda → Raiz → Direita",
        "postorder_hint": "Esquerda → Direita → Raiz",
        "empty": "⚠ Insira números antes de verificar.",
        "correct": "✅ CORRETO! Bom trabalho.",
        "wrong": "❌ Errado.\nSua: {user}\nCorreta: {correct}",
        "format_error": "⚠ Formato inválido. Apenas números separados por espaços ou vírgulas.",
        "nodes": "Nós: {n}",
        "rb_title": "Árvores Rubro-Negras",
        "rb_question": "A árvore acima é uma árvore rubro-negra VÁLIDA?",
        "rb_yes": "✅ Sim, válida",
        "rb_no": "❌ Não, inválida",
        "rb_new": "🔄 Nova Árvore",
        "rb_correct_valid": "✅ CORRETO! É uma árvore rubro-negra válida.",
        "rb_correct_invalid": "✅ CORRETO! Não é válida porque {reason}.",
        "rb_wrong_was_valid": "❌ Errado. A árvore ERA uma rubro-negra válida.",
        "rb_wrong_was_invalid": "❌ Errado. A árvore NÃO era válida porque {reason}.",
        "rb_reason_root": "a raiz deve ser PRETA",
        "rb_reason_red_red": "um nó VERMELHO tem um filho VERMELHO",
        "rb_reason_bh": "os caminhos têm alturas pretas diferentes",
        "rb_rules_title": "Propriedades de uma árvore rubro-negra:",
        "rb_rule_1": "1) Cada nó é vermelho ou preto.",
        "rb_rule_2": "2) A raiz é preta.",
        "rb_rule_3": "3) As folhas NIL (quadrados pretos) são pretas.",
        "rb_rule_4": "4) Um nó vermelho não pode ter filhos vermelhos.",
        "rb_rule_5": "5) Cada caminho de um nó até folhas NIL contém o mesmo número de nós pretos.",
        "async_title": "Notação Assintótica",
        "async_question": "Qual é a complexidade temporal do seguinte algoritmo?",
        "async_new": "🔄 Novo Exercício",
        "async_pick": "Escolha sua resposta clicando em uma das opções:",
        "async_correct": "✅ CORRETO! A complexidade é {ans}.\n{explain}",
        "async_wrong": "❌ Errado. A resposta correta é {ans}.\n{explain}",
        "expl_const": "Operação constante: não depende do tamanho da entrada.",
        "expl_loop": "Um único laço que percorre a entrada uma vez.",
        "expl_nested": "Dois laços aninhados sobre n elementos: n × n.",
        "expl_binsearch": "A cada passo o espaço de busca é dividido pela metade.",
        "expl_fib": "Recursão binária sem memoização: 2 chamadas por nível.",
        "expl_mergesort": "Recursão dividindo a entrada + merge linear.",
        "expl_triple": "Três laços aninhados sobre n elementos: n × n × n.",
        "expl_logn": "O índice dobra a cada iteração (log₂ n passos).",
        "expl_nlogn": "Laço externo O(n) com laço interno O(log n).",
        "expl_harmonic": "A soma 1 + 1/2 + ... + 1/n é O(log n), mas o laço externo é O(n).",
        "expl_sumi": "O laço interno executa i vezes: 1+2+...+n = n(n+1)/2.",
    },
}

for _lang, _kvs in SORT_TRANSLATIONS.items():
    TRANSLATIONS[_lang].update(_kvs)

for _lang, _kvs in BFS_TRANSLATIONS.items():
    TRANSLATIONS[_lang].update(_kvs)

for _lang, _kvs in SORT_TABLE_TRANSLATIONS.items():
    TRANSLATIONS[_lang].update(_kvs)

for _lang, _kvs in SORT_TABLE_ROW_TRANSLATIONS.items():
    TRANSLATIONS[_lang].update(_kvs)

for _lang, _kvs in RANDOM_MIX_TRANSLATIONS.items():
    TRANSLATIONS[_lang].update(_kvs)

for _lang, _kvs in stats_tracker.STATS_TRANSLATIONS.items():
    TRANSLATIONS[_lang].update(_kvs)


OPTIONS = ["O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n²)", "O(n³)", "O(2ⁿ)"]

ASYNC_FUNC_NAMES = ["f", "compute", "process", "analyze", "check", "scan", "run", "solve"]
ASYNC_ARR_NAMES = ["arr", "data", "lst", "items", "values"]
ASYNC_N_NAMES = ["n", "size", "length"]
ASYNC_TARGET_NAMES = ["target", "key", "value"]


def _async_names():
    return {
        "fn": random.choice(ASYNC_FUNC_NAMES),
        "arr": random.choice(ASYNC_ARR_NAMES),
        "n": random.choice(ASYNC_N_NAMES),
        "k": random.choice(ASYNC_TARGET_NAMES),
    }


def _gen_O1():
    s = _async_names()
    c = random.randint(2, 99)
    variants = [
        f"def {s['fn']}({s['arr']}):\n    if not {s['arr']}:\n        return None\n    return {s['arr']}[0]",
        f"def {s['fn']}({s['arr']}):\n    return {s['arr']}[-1] if {s['arr']} else None",
        f"def {s['fn']}(x, y):\n    return x * y + {c}",
        f"def {s['fn']}({s['arr']}):\n    if len({s['arr']}) < 2:\n        return 0\n    return {s['arr']}[0] + {s['arr']}[-1]",
        f"def {s['fn']}({s['n']}):\n    total = 0\n    for i in range({random.choice([5, 10, 16, 100])}):\n        total += i * i\n    return total",
        f"def {s['fn']}(a, b):\n    a, b = b, a\n    return a - b",
        f"def {s['fn']}({s['arr']}):\n    return {s['arr']}[len({s['arr']}) // 2]",
    ]
    return random.choice(variants), "O(1)", "expl_const"


def _gen_On():
    s = _async_names()
    variants = [
        f"def {s['fn']}({s['arr']}):\n    total = 0\n    for x in {s['arr']}:\n        total += x\n    return total",
        f"def {s['fn']}({s['arr']}, {s['k']}):\n    for i, x in enumerate({s['arr']}):\n        if x == {s['k']}:\n            return i\n    return -1",
        f"def {s['fn']}({s['arr']}):\n    result = []\n    for x in {s['arr']}:\n        result.append(x * 2)\n    return result",
        f"def {s['fn']}({s['n']}):\n    count = 0\n    for i in range({s['n']}):\n        count += i\n    return count",
        f"def {s['fn']}({s['arr']}):\n    best = {s['arr']}[0]\n    for x in {s['arr']}:\n        if x > best:\n            best = x\n    return best",
        f"def {s['fn']}({s['arr']}):\n    n = len({s['arr']})\n    i = 0\n    while i < n:\n        if {s['arr']}[i] < 0:\n            return False\n        i += 1\n    return True",
        f"def {s['fn']}({s['arr']}):\n    s = 0\n    for x in {s['arr']}:\n        s += x * x\n    return s",
    ]
    return random.choice(variants), "O(n)", "expl_loop"


def _gen_Ologn():
    s = _async_names()
    factor = random.choice([2, 3, 4])
    variants = [
        (f"def {s['fn']}({s['n']}):\n    count = 0\n    while {s['n']} > 1:\n        {s['n']} //= 2\n        count += 1\n    return count", "expl_logn"),
        (f"def {s['fn']}({s['n']}):\n    i = 1\n    while i < {s['n']}:\n        i *= {factor}\n    return i", "expl_logn"),
        (f"def {s['fn']}({s['arr']}, {s['k']}):\n    lo, hi = 0, len({s['arr']})\n    while lo < hi:\n        mid = (lo + hi) // 2\n        if {s['arr']}[mid] == {s['k']}:\n            return mid\n        elif {s['arr']}[mid] < {s['k']}:\n            lo = mid + 1\n        else:\n            hi = mid\n    return -1", "expl_binsearch"),
        (f"def {s['fn']}({s['n']}):\n    result = 0\n    i = {s['n']}\n    while i > 0:\n        result += 1\n        i //= 2\n    return result", "expl_logn"),
    ]
    code, key = random.choice(variants)
    return code, "O(log n)", key


def _gen_Onlogn():
    s = _async_names()
    factor = random.choice([2, 3])
    variants = [
        (f"def {s['fn']}({s['arr']}):\n    n = len({s['arr']})\n    for i in range(n):\n        j = 1\n        while j < n:\n            j *= {factor}", "expl_nlogn"),
        (f"def {s['fn']}({s['arr']}):\n    if len({s['arr']}) <= 1:\n        return {s['arr']}\n    mid = len({s['arr']}) // 2\n    left = {s['fn']}({s['arr']}[:mid])\n    right = {s['fn']}({s['arr']}[mid:])\n    return merge(left, right)", "expl_mergesort"),
        (f"def {s['fn']}({s['n']}):\n    count = 0\n    for i in range(1, {s['n']} + 1):\n        j = i\n        while j > 0:\n            count += 1\n            j //= 2\n    return count", "expl_harmonic"),
        (f"def {s['fn']}({s['arr']}):\n    n = len({s['arr']})\n    for i in range(n):\n        lo, hi = 0, n\n        while lo < hi:\n            mid = (lo + hi) // 2\n            if {s['arr']}[mid] == i:\n                break\n            elif {s['arr']}[mid] < i:\n                lo = mid + 1\n            else:\n                hi = mid", "expl_nlogn"),
    ]
    code, key = random.choice(variants)
    return code, "O(n log n)", key


def _gen_On2():
    s = _async_names()
    variants = [
        (f"def {s['fn']}({s['arr']}):\n    n = len({s['arr']})\n    for i in range(n):\n        for j in range(n):\n            if {s['arr']}[i] + {s['arr']}[j] == 0:\n                return True\n    return False", "expl_nested"),
        (f"def {s['fn']}({s['n']}):\n    count = 0\n    for i in range({s['n']}):\n        for j in range(i):\n            count += 1\n    return count", "expl_sumi"),
        (f"def {s['fn']}({s['arr']}):\n    n = len({s['arr']})\n    for i in range(n):\n        for j in range(i + 1, n):\n            if {s['arr']}[i] == {s['arr']}[j]:\n                return True\n    return False", "expl_sumi"),
        (f"def {s['fn']}({s['arr']}):\n    n = len({s['arr']})\n    best = 0\n    for i in range(n):\n        for j in range(n):\n            best = max(best, abs({s['arr']}[i] - {s['arr']}[j]))\n    return best", "expl_nested"),
        (f"def {s['fn']}({s['arr']}):\n    n = len({s['arr']})\n    for i in range(n):\n        for j in range(n):\n            if i != j and {s['arr']}[i] == {s['arr']}[j]:\n                return True\n    return False", "expl_nested"),
    ]
    code, key = random.choice(variants)
    return code, "O(n²)", key


def _gen_On3():
    s = _async_names()
    variants = [
        f"def {s['fn']}({s['arr']}):\n    n = len({s['arr']})\n    for i in range(n):\n        for j in range(n):\n            for k in range(n):\n                if {s['arr']}[i] + {s['arr']}[j] + {s['arr']}[k] == 0:\n                    return True\n    return False",
        f"def {s['fn']}({s['n']}):\n    count = 0\n    for i in range({s['n']}):\n        for j in range({s['n']}):\n            for k in range({s['n']}):\n                count += 1\n    return count",
        f"def {s['fn']}(A, B):\n    n = len(A)\n    result = [[0] * n for _ in range(n)]\n    for i in range(n):\n        for j in range(n):\n            for k in range(n):\n                result[i][j] += A[i][k] * B[k][j]\n    return result",
    ]
    return random.choice(variants), "O(n³)", "expl_triple"


def _gen_O2n():
    s = _async_names()
    variants = [
        f"def {s['fn']}({s['n']}):\n    if {s['n']} <= 1:\n        return {s['n']}\n    return {s['fn']}({s['n']} - 1) + {s['fn']}({s['n']} - 2)",
        f"def {s['fn']}({s['n']}):\n    if {s['n']} == 0:\n        return 1\n    return {s['fn']}({s['n']} - 1) + {s['fn']}({s['n']} - 1)",
        f"def {s['fn']}({s['n']}):\n    if {s['n']} <= 0:\n        return 0\n    return 1 + {s['fn']}({s['n']} - 1) + {s['fn']}({s['n']} - 1)",
    ]
    return random.choice(variants), "O(2ⁿ)", "expl_fib"


ASYNC_GENERATORS = {
    "O(1)": _gen_O1,
    "O(log n)": _gen_Ologn,
    "O(n)": _gen_On,
    "O(n log n)": _gen_Onlogn,
    "O(n²)": _gen_On2,
    "O(n³)": _gen_On3,
    "O(2ⁿ)": _gen_O2n,
}


def generate_async_exercise(last_answer=None):
    classes = list(ASYNC_GENERATORS.keys())
    if last_answer in classes and len(classes) > 1:
        classes = [c for c in classes if c != last_answer]
    chosen = random.choice(classes)
    code, ans, key = ASYNC_GENERATORS[chosen]()
    return {"code": code, "answer": ans, "explain_key": key}


class Nodo:
    __slots__ = ("valore", "sinistra", "destra", "x", "y", "colore")

    def __init__(self, valore, colore=None):
        self.valore = valore
        self.colore = colore
        self.sinistra = None
        self.destra = None
        self.x = 0.0
        self.y = 0.0


def _rb_check(node):
    if node is None:
        return True, None, 1
    if node.colore == "red":
        if (node.sinistra and node.sinistra.colore == "red") or (
            node.destra and node.destra.colore == "red"
        ):
            return False, "rb_reason_red_red", 0
    lv, lr, lbh = _rb_check(node.sinistra)
    if not lv:
        return False, lr, 0
    rv, rr, rbh = _rb_check(node.destra)
    if not rv:
        return False, rr, 0
    if lbh != rbh:
        return False, "rb_reason_bh", 0
    return True, None, lbh + (1 if node.colore == "black" else 0)


def is_valid_rb(root):
    if root is None:
        return True, None
    if root.colore != "black":
        return False, "rb_reason_root"
    valid, reason, _ = _rb_check(root)
    return valid, reason


def _collect_nodes(node, out):
    if node is None:
        return
    out.append(node)
    _collect_nodes(node.sinistra, out)
    _collect_nodes(node.destra, out)


def _build_random_structure(num_nodes):
    values = random.sample(range(1, 100), num_nodes)
    root = Nodo(values[0])
    leaves_with_room = [root]
    for v in values[1:]:
        random.shuffle(leaves_with_room)
        placed = False
        for parent in leaves_with_room:
            empty_sides = []
            if parent.sinistra is None:
                empty_sides.append("L")
            if parent.destra is None:
                empty_sides.append("R")
            if empty_sides:
                side = random.choice(empty_sides)
                child = Nodo(v)
                if side == "L":
                    parent.sinistra = child
                else:
                    parent.destra = child
                leaves_with_room.append(child)
                if parent.sinistra is not None and parent.destra is not None:
                    leaves_with_room.remove(parent)
                placed = True
                break
        if not placed:
            break
    return root


def generate_rb_exercise():
    """Generate a small tree with random coloring; aims for both valid and invalid cases."""
    want_valid = random.random() < 0.5

    for _outer in range(30):
        num_nodes = random.choice([3, 4, 5, 5, 6, 7])
        root = _build_random_structure(num_nodes)
        nodes = []
        _collect_nodes(root, nodes)

        for _ in range(800):
            for n in nodes:
                n.colore = random.choice(["red", "black"])
            if want_valid:
                nodes[0].colore = "black"
            valid, reason = is_valid_rb(root)
            if valid == want_valid:
                return root, valid, reason

    # Fallback: simple valid all-black tree
    root = Nodo(random.randint(1, 99), "black")
    root.sinistra = Nodo(random.randint(1, 99), "black")
    root.destra = Nodo(random.randint(1, 99), "black")
    return root, True, None


class MainController:
    def __init__(self, root):
        self.root = root
        self.lang = "it"
        self.current_screen = None
        self.root.geometry("1100x800")
        self.root.configure(bg="#f0f0f0")
        self._update_title()
        self.show_menu()

    def t(self, key, **fmt):
        s = TRANSLATIONS[self.lang].get(key, key)
        return s.format(**fmt) if fmt else s

    def _update_title(self):
        self.root.title(self.t("app_title"))

    def _swap(self, cls):
        if self.current_screen is not None:
            self.current_screen.destroy()
        self.current_screen = cls(self.root, self)
        self.current_screen.pack(expand=True, fill=tk.BOTH)

    def show_menu(self):
        self._swap(MenuScreen)

    def show_dfs(self):
        self._swap(DFSScreen)

    def show_rb(self):
        self._swap(RBScreen)

    def show_async(self):
        self._swap(AsyncScreen)

    def show_sort(self):
        self._swap(SortingScreen)

    def show_bfs(self):
        self._swap(BFSScreen)

    def show_sort_table(self):
        self._swap(SortingTableScreen)

    def show_random(self):
        self._swap(RandomMixScreen)

    def set_language(self, lang_code):
        self.lang = lang_code
        self._update_title()

    def language_options(self):
        return [(code, TRANSLATIONS[code]["lang_name"]) for code in TRANSLATIONS]


class MenuScreen(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root, bg="#f0f0f0")
        self.controller = controller
        self._build()

    def _build(self):
        top = tk.Frame(self, bg="#e0e0e0", pady=10, padx=12, relief=tk.RAISED, bd=2)
        top.pack(fill=tk.X, padx=10, pady=(10, 5))

        tk.Label(
            top, text=self.controller.t("language"), bg="#e0e0e0",
            font=("Arial", 11, "bold"),
        ).pack(side=tk.LEFT)
        self.var_lang = tk.StringVar(value=TRANSLATIONS[self.controller.lang]["lang_name"])
        cb = ttk.Combobox(
            top, textvariable=self.var_lang, width=14, state="readonly",
            values=[TRANSLATIONS[k]["lang_name"] for k in TRANSLATIONS],
        )
        cb.pack(side=tk.LEFT, padx=8)
        cb.bind("<<ComboboxSelected>>", self._on_lang)

        tk.Label(
            self, text=self.controller.t("menu_title"),
            font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#222",
        ).pack(pady=(20, 4))
        tk.Label(
            self, text=self.controller.t("menu_subtitle"),
            font=("Arial", 11, "italic"), bg="#f0f0f0", fg="#666",
        ).pack(pady=(0, 16))

        btn_frame = tk.Frame(self, bg="#f0f0f0")
        btn_frame.pack(pady=10)

        configs = [
            ("menu_random", "#3F51B5", self.controller.show_random),
            ("menu_dfs", "#4CAF50", self.controller.show_dfs),
            ("menu_bfs", "#00BCD4", self.controller.show_bfs),
            ("menu_rb", "#E91E63", self.controller.show_rb),
            ("menu_async", "#9C27B0", self.controller.show_async),
            ("menu_sort", "#FF9800", self.controller.show_sort),
            ("menu_sort_table", "#607D8B", self.controller.show_sort_table),
        ]
        for key, color, cmd in configs:
            tk.Button(
                btn_frame, text=self.controller.t(key), command=cmd,
                bg=color, fg="white", font=("Arial", 12, "bold"),
                width=34, height=2, relief=tk.RAISED, bd=3,
                activebackground=color, cursor="hand2", justify="center",
            ).pack(pady=5)

        self._build_stats_panel()

    def _build_stats_panel(self):
        panel = tk.Frame(self, bg="#f0f0f0")
        panel.pack(pady=(12, 16))

        if stats_tracker.is_enabled():
            tk.Label(
                panel, text=self.controller.t("stats_active"),
                font=("Arial", 10, "bold"), bg="#f0f0f0", fg="#2E7D32",
            ).pack(pady=(0, 4))
            row = tk.Frame(panel, bg="#f0f0f0")
            row.pack()
            tk.Button(
                row, text=self.controller.t("stats_view_btn"),
                command=self._show_stats_window,
                bg="#2E7D32", fg="white", font=("Arial", 10, "bold"),
                padx=10, pady=4, cursor="hand2",
            ).pack(side=tk.LEFT, padx=4)
            tk.Button(
                row, text=self.controller.t("stats_reset_btn"),
                command=self._reset_stats,
                bg="#B71C1C", fg="white", font=("Arial", 10, "bold"),
                padx=10, pady=4, cursor="hand2",
            ).pack(side=tk.LEFT, padx=4)
            tk.Label(
                panel,
                text=self.controller.t("stats_path_label", path=stats_tracker.STATS_FILE),
                font=("Arial", 8, "italic"), bg="#f0f0f0", fg="#888",
            ).pack(pady=(4, 0))
        else:
            tk.Label(
                panel, text=self.controller.t("stats_inactive"),
                font=("Arial", 10, "italic"), bg="#f0f0f0", fg="#888",
            ).pack(pady=(0, 4))
            tk.Button(
                panel, text=self.controller.t("stats_create_btn"),
                command=self._create_stats_file,
                bg="#2E7D32", fg="white", font=("Arial", 10, "bold"),
                padx=10, pady=4, cursor="hand2",
            ).pack()
            tk.Label(
                panel,
                text=self.controller.t("stats_path_label", path=stats_tracker.STATS_FILE),
                font=("Arial", 8, "italic"), bg="#f0f0f0", fg="#888",
            ).pack(pady=(4, 0))

    def _create_stats_file(self):
        ok, err = stats_tracker.create_file()
        if ok:
            from tkinter import messagebox
            messagebox.showinfo(
                self.controller.t("stats_window_title"),
                self.controller.t("stats_create_ok", path=stats_tracker.STATS_FILE),
            )
            self._rebuild()
        else:
            from tkinter import messagebox
            messagebox.showerror(
                self.controller.t("stats_window_title"),
                self.controller.t("stats_create_err", err=err),
            )

    def _reset_stats(self):
        from tkinter import messagebox
        if messagebox.askyesno(
            self.controller.t("stats_window_title"),
            self.controller.t("stats_reset_confirm"),
        ):
            stats_tracker.reset()

    def _show_stats_window(self):
        win = tk.Toplevel(self)
        win.title(self.controller.t("stats_window_title"))
        win.configure(bg="#f0f0f0")
        win.geometry("640x440")

        stats = stats_tracker.load()
        total_right = sum(stats[c]["right"] for c in stats_tracker.CATEGORIES)
        total_wrong = sum(stats[c]["wrong"] for c in stats_tracker.CATEGORIES)
        grand_total = total_right + total_wrong

        tk.Label(
            win, text=self.controller.t("stats_window_title"),
            font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#222",
        ).pack(pady=(10, 4))
        tk.Label(
            win,
            text=self.controller.t("stats_path_label", path=stats_tracker.STATS_FILE),
            font=("Arial", 8, "italic"), bg="#f0f0f0", fg="#888",
        ).pack(pady=(0, 8))

        if grand_total == 0:
            tk.Label(
                win, text=self.controller.t("stats_no_data"),
                font=("Arial", 11, "italic"), bg="#f0f0f0", fg="#666",
            ).pack(pady=20)
        else:
            tree_frame = tk.Frame(win, bg="#f0f0f0")
            tree_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=4)
            cols = ("cat", "right", "wrong", "pct", "weight")
            tv = ttk.Treeview(tree_frame, columns=cols, show="headings", height=10)
            tv.heading("cat", text=self.controller.t("stats_header_cat"))
            tv.heading("right", text=self.controller.t("stats_header_right"))
            tv.heading("wrong", text=self.controller.t("stats_header_wrong"))
            tv.heading("pct", text=self.controller.t("stats_header_pct"))
            tv.heading("weight", text=self.controller.t("stats_header_weight"))
            tv.column("cat", width=200, anchor="w")
            for c in ("right", "wrong", "pct", "weight"):
                tv.column(c, width=90, anchor="center")
            tv.pack(expand=True, fill=tk.BOTH)
            for cat in stats_tracker.CATEGORIES:
                d = stats[cat]
                total = d["right"] + d["wrong"]
                pct = (d["wrong"] / total * 100) if total else 0.0
                w = stats_tracker.weight_for(d)
                tv.insert("", "end", values=(
                    self.controller.t(f"cat_{cat}"),
                    d["right"],
                    d["wrong"],
                    f"{pct:.0f}%" if total else "—",
                    f"{w:.2f}",
                ))
            grand_pct = (total_wrong / grand_total * 100) if grand_total else 0.0
            tv.insert("", "end", values=(
                self.controller.t("stats_total_row"),
                total_right, total_wrong,
                f"{grand_pct:.0f}%", "",
            ))

        tk.Button(
            win, text=self.controller.t("stats_close_btn"),
            command=win.destroy,
            bg="#757575", fg="white", font=("Arial", 10, "bold"),
            padx=12, pady=4, cursor="hand2",
        ).pack(pady=10)

    def _rebuild(self):
        for w in self.winfo_children():
            w.destroy()
        self._build()

    def _on_lang(self, _e=None):
        chosen = self.var_lang.get()
        for code, data in TRANSLATIONS.items():
            if data["lang_name"] == chosen:
                self.controller.set_language(code)
                self._rebuild()
                break


class DFSScreen(tk.Frame):
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
        self.tipo_visita_key = "preorder"
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
        self.var_lang = tk.StringVar(value=TRANSLATIONS[self.controller.lang]["lang_name"])
        self.cb_lang = ttk.Combobox(
            top, textvariable=self.var_lang, width=12, state="readonly",
            values=[TRANSLATIONS[k]["lang_name"] for k in TRANSLATIONS],
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
            top, command=self.genera_nuovo_quiz, bg="#4CAF50", fg="white",
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
        tr = TRANSLATIONS[self.controller.lang]
        self.btn_back.config(text=tr["back"])
        self.lbl_lang.config(text=tr["language"])
        self.lbl_depth.config(text=tr["depth"])
        self.chk_bilanciato.config(text=tr["balanced"])
        self.chk_hint.config(text=tr["show_hint"])
        self.btn_genera.config(text=tr["generate"])
        self.btn_zoom_in.config(text=tr["zoom_in"])
        self.btn_zoom_out.config(text=tr["zoom_out"])
        self.btn_zoom_reset.config(text=tr["zoom_reset"])
        self.btn_fit.config(text=tr["fit"])
        self.lbl_seq.config(text=tr["your_sequence"])
        self.btn_verifica.config(text=tr["verify"])
        self.var_lang.set(tr["lang_name"])
        self._update_question_label()
        self._update_node_count()

    def _on_language_change(self, _event=None):
        chosen = self.var_lang.get()
        for code, data in TRANSLATIONS.items():
            if data["lang_name"] == chosen:
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

        nodo = Nodo(valore)
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
            fill="#E1F5FE", outline="#0288D1", width=2,
        )
        self.canvas.create_text(
            nodo.x, nodo.y, text=str(nodo.valore), font=("Arial", 11, "bold"), fill="#01579B",
        )

    def _count_nodes(self, nodo):
        if not nodo:
            return 0
        return 1 + self._count_nodes(nodo.sinistra) + self._count_nodes(nodo.destra)

    def pre_order(self, nodo):
        return [nodo.valore] + self.pre_order(nodo.sinistra) + self.pre_order(nodo.destra) if nodo else []

    def in_order(self, nodo):
        return self.in_order(nodo.sinistra) + [nodo.valore] + self.in_order(nodo.destra) if nodo else []

    def post_order(self, nodo):
        return self.post_order(nodo.sinistra) + self.post_order(nodo.destra) + [nodo.valore] if nodo else []

    def genera_nuovo_quiz(self):
        self.canvas.delete("all")
        self.entry_risposta.delete(0, tk.END)
        self.lbl_feedback.config(text="")
        self.zoom_level = 1.0
        self.stats_recorded = False

        for _ in range(20):
            self.albero = self.genera_albero()
            if self.albero and self._count_nodes(self.albero) >= 3:
                break
        else:
            valori = random.sample(range(1, 100), 3)
            self.albero = Nodo(valori[0])
            self.albero.sinistra = Nodo(valori[1])
            self.albero.destra = Nodo(valori[2])

        width, height, _ = self._layout(self.albero)
        self._disegna(self.albero)
        self.canvas.configure(scrollregion=(0, 0, width, height))
        self._update_node_count()

        algoritmi = {
            "preorder": self.pre_order(self.albero),
            "inorder": self.in_order(self.albero),
            "postorder": self.post_order(self.albero),
        }
        self.tipo_visita_key = random.choice(list(algoritmi.keys()))
        self.sequenza_corretta = algoritmi[self.tipo_visita_key]
        self._update_question_label()
        self.entry_risposta.focus()
        self.after(50, self._fit_to_view)

    def _update_question_label(self):
        if not hasattr(self, "tipo_visita_key"):
            return
        name = self.t(self.tipo_visita_key)
        if self.var_hint.get():
            hint = self.t(f"{self.tipo_visita_key}_hint")
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
        correct = sequenza_utente == self.sequenza_corretta
        if correct:
            self.lbl_feedback.config(text=self.t("correct"), fg="#4CAF50")
        else:
            self.lbl_feedback.config(
                text=self.t("wrong", user=sequenza_utente, correct=self.sequenza_corretta),
                fg="#F44336",
            )
        if not self.stats_recorded:
            stats_tracker.record("dfs", correct)
            self.stats_recorded = True

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


class RBScreen(tk.Frame):
    H_SPACING = 65
    V_SPACING = 85
    MARGIN = 50
    RAGGIO = 22
    NIL_SIZE = 8

    def __init__(self, root, controller):
        super().__init__(root, bg="#f0f0f0")
        self.controller = controller
        self.albero = None
        self.is_valid = False
        self.reason = None
        self.answered = False
        self._build_ui()
        self._apply_language()
        self.genera_nuovo_albero()

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
        self.var_lang = tk.StringVar(value=TRANSLATIONS[self.controller.lang]["lang_name"])
        self.cb_lang = ttk.Combobox(
            top, textvariable=self.var_lang, width=12, state="readonly",
            values=[TRANSLATIONS[k]["lang_name"] for k in TRANSLATIONS],
        )
        self.cb_lang.pack(side=tk.LEFT, padx=(4, 15))
        self.cb_lang.bind("<<ComboboxSelected>>", self._on_language_change)

        self.lbl_title = tk.Label(
            top, bg="#e0e0e0", font=("Arial", 13, "bold"), fg="#333",
        )
        self.lbl_title.pack(side=tk.LEFT, padx=20)

        self.btn_new = tk.Button(
            top, command=self.genera_nuovo_albero, bg="#E91E63", fg="white",
            font=("Arial", 10, "bold"), padx=8,
        )
        self.btn_new.pack(side=tk.RIGHT, padx=5)

        canvas_frame = tk.Frame(self, bd=2, relief=tk.SUNKEN)
        canvas_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)
        self.canvas = tk.Canvas(canvas_frame, bg="white", highlightthickness=0)
        self.canvas.pack(expand=True, fill=tk.BOTH)

        bottom = tk.Frame(self, bg="#f0f0f0", pady=8)
        bottom.pack(fill=tk.X, padx=10, side=tk.BOTTOM)

        self.lbl_question = tk.Label(
            bottom, text="", font=("Arial", 13, "bold"), bg="#f0f0f0", fg="#333",
            wraplength=1000, justify="center",
        )
        self.lbl_question.pack(pady=(0, 8))

        btn_row = tk.Frame(bottom, bg="#f0f0f0")
        btn_row.pack()
        self.btn_yes = tk.Button(
            btn_row, command=lambda: self.verifica(True), bg="#4CAF50", fg="white",
            font=("Arial", 12, "bold"), padx=18, pady=4,
        )
        self.btn_yes.pack(side=tk.LEFT, padx=10)
        self.btn_no = tk.Button(
            btn_row, command=lambda: self.verifica(False), bg="#F44336", fg="white",
            font=("Arial", 12, "bold"), padx=18, pady=4,
        )
        self.btn_no.pack(side=tk.LEFT, padx=10)

        self.lbl_feedback = tk.Label(
            bottom, text="", font=("Arial", 11, "bold"), bg="#f0f0f0",
            wraplength=1000, justify="center",
        )
        self.lbl_feedback.pack(pady=8)

        self.lbl_rules = tk.Label(
            bottom, text="", font=("Arial", 9), bg="#f0f0f0", fg="#666",
            wraplength=1000, justify="left",
        )
        self.lbl_rules.pack(pady=(0, 4))

    def _apply_language(self):
        tr = TRANSLATIONS[self.controller.lang]
        self.btn_back.config(text=tr["back"])
        self.lbl_lang.config(text=tr["language"])
        self.lbl_title.config(text=tr["rb_title"])
        self.btn_new.config(text=tr["rb_new"])
        self.lbl_question.config(text=tr["rb_question"])
        self.btn_yes.config(text=tr["rb_yes"])
        self.btn_no.config(text=tr["rb_no"])
        rules = "\n".join(
            [tr["rb_rules_title"], tr["rb_rule_1"], tr["rb_rule_2"],
             tr["rb_rule_3"], tr["rb_rule_4"], tr["rb_rule_5"]]
        )
        self.lbl_rules.config(text=rules)
        self.var_lang.set(tr["lang_name"])

    def _on_language_change(self, _e=None):
        chosen = self.var_lang.get()
        for code, data in TRANSLATIONS.items():
            if data["lang_name"] == chosen:
                self.controller.set_language(code)
                break
        self._apply_language()

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
        height = 2 * self.MARGIN + (max_depth[0] + 1) * self.V_SPACING + 2 * self.RAGGIO
        return width, height

    def _draw_nil(self, x, y):
        s = self.NIL_SIZE
        self.canvas.create_rectangle(
            x - s, y - s, x + s, y + s,
            fill="#222", outline="#000", width=1,
        )
        self.canvas.create_text(
            x, y, text="NIL", font=("Arial", 6, "bold"), fill="white",
        )

    def _disegna(self, nodo):
        if nodo is None:
            return

        # Draw edges to children (or NIL placeholders)
        for child, dx in [(nodo.sinistra, -1), (nodo.destra, 1)]:
            if child:
                self.canvas.create_line(
                    nodo.x, nodo.y, child.x, child.y, width=2, fill="#555",
                )
                self._disegna(child)
            else:
                # NIL leaf
                nil_x = nodo.x + dx * self.H_SPACING * 0.45
                nil_y = nodo.y + self.V_SPACING * 0.65
                self.canvas.create_line(
                    nodo.x, nodo.y, nil_x, nil_y, width=1, fill="#999", dash=(3, 2),
                )
                self._draw_nil(nil_x, nil_y)

        # Draw the node itself
        r = self.RAGGIO
        if nodo.colore == "red":
            fill, outline, text_color = "#E53935", "#B71C1C", "white"
        else:
            fill, outline, text_color = "#212121", "#000000", "white"

        self.canvas.create_oval(
            nodo.x - r, nodo.y - r, nodo.x + r, nodo.y + r,
            fill=fill, outline=outline, width=2,
        )
        self.canvas.create_text(
            nodo.x, nodo.y, text=str(nodo.valore),
            font=("Arial", 12, "bold"), fill=text_color,
        )

    def genera_nuovo_albero(self):
        self.canvas.delete("all")
        self.lbl_feedback.config(text="")
        self.answered = False
        self.btn_yes.config(state=tk.NORMAL)
        self.btn_no.config(state=tk.NORMAL)

        self.albero, self.is_valid, self.reason = generate_rb_exercise()
        width, height = self._layout(self.albero)
        self._disegna(self.albero)
        # Center contents in canvas
        self.canvas.update_idletasks()
        cw = self.canvas.winfo_width() or width
        ch = self.canvas.winfo_height() or height
        offset_x = max((cw - width) // 2, 0)
        offset_y = max((ch - height) // 2, 0)
        if offset_x or offset_y:
            self.canvas.move("all", offset_x, offset_y)

    def verifica(self, user_says_valid):
        if self.answered:
            return
        self.answered = True
        self.btn_yes.config(state=tk.DISABLED)
        self.btn_no.config(state=tk.DISABLED)

        correct = (user_says_valid == self.is_valid)
        stats_tracker.record("rb", correct)
        reason_text = self.t(self.reason) if self.reason else ""

        if correct and self.is_valid:
            self.lbl_feedback.config(text=self.t("rb_correct_valid"), fg="#4CAF50")
        elif correct and not self.is_valid:
            self.lbl_feedback.config(
                text=self.t("rb_correct_invalid", reason=reason_text), fg="#4CAF50",
            )
        elif not correct and self.is_valid:
            self.lbl_feedback.config(text=self.t("rb_wrong_was_valid"), fg="#F44336")
        else:
            self.lbl_feedback.config(
                text=self.t("rb_wrong_was_invalid", reason=reason_text), fg="#F44336",
            )


class AsyncScreen(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root, bg="#f0f0f0")
        self.controller = controller
        self.current = None
        self.answered = False
        self.option_buttons = []
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
        self.var_lang = tk.StringVar(value=TRANSLATIONS[self.controller.lang]["lang_name"])
        self.cb_lang = ttk.Combobox(
            top, textvariable=self.var_lang, width=12, state="readonly",
            values=[TRANSLATIONS[k]["lang_name"] for k in TRANSLATIONS],
        )
        self.cb_lang.pack(side=tk.LEFT, padx=(4, 15))
        self.cb_lang.bind("<<ComboboxSelected>>", self._on_language_change)

        self.lbl_title = tk.Label(top, bg="#e0e0e0", font=("Arial", 13, "bold"), fg="#333")
        self.lbl_title.pack(side=tk.LEFT, padx=20)

        self.btn_new = tk.Button(
            top, command=self.nuovo_esercizio, bg="#9C27B0", fg="white",
            font=("Arial", 10, "bold"), padx=8,
        )
        self.btn_new.pack(side=tk.RIGHT, padx=5)

        center = tk.Frame(self, bg="#f0f0f0")
        center.pack(expand=True, fill=tk.BOTH, padx=10, pady=8)

        self.lbl_question = tk.Label(
            center, text="", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#333",
            wraplength=1000, justify="center",
        )
        self.lbl_question.pack(pady=(4, 8))

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
        for opt in OPTIONS:
            b = tk.Button(
                self.options_frame, text=opt, command=lambda o=opt: self.verifica(o),
                bg="#2196F3", fg="white", font=("Arial", 12, "bold"),
                width=10, padx=4, pady=4,
            )
            b.pack(side=tk.LEFT, padx=4)
            self.option_buttons.append(b)

        self.lbl_feedback = tk.Label(
            bottom, text="", font=("Arial", 11, "bold"), bg="#f0f0f0",
            wraplength=1000, justify="center",
        )
        self.lbl_feedback.pack(pady=8)

    def _apply_language(self):
        tr = TRANSLATIONS[self.controller.lang]
        self.btn_back.config(text=tr["back"])
        self.lbl_lang.config(text=tr["language"])
        self.lbl_title.config(text=tr["async_title"])
        self.btn_new.config(text=tr["async_new"])
        self.lbl_question.config(text=tr["async_question"])
        self.lbl_pick.config(text=tr["async_pick"])
        self.var_lang.set(tr["lang_name"])

    def _on_language_change(self, _e=None):
        chosen = self.var_lang.get()
        for code, data in TRANSLATIONS.items():
            if data["lang_name"] == chosen:
                self.controller.set_language(code)
                break
        self._apply_language()
        # If we already showed a feedback for current exercise, refresh in new language
        if self.answered and self.current:
            explain = self.t(self.current["explain_key"])
            self.lbl_feedback.config(
                text=self.lbl_feedback.cget("text").split("\n")[0] + "\n" + explain
            )

    def nuovo_esercizio(self):
        self.answered = False
        self.lbl_feedback.config(text="")
        for b in self.option_buttons:
            b.config(state=tk.NORMAL, bg="#2196F3")

        last = self.current["answer"] if self.current else None
        self.current = generate_async_exercise(last_answer=last)
        self.text_code.configure(state=tk.NORMAL)
        self.text_code.delete("1.0", tk.END)
        self.text_code.insert("1.0", self.current["code"])
        self.text_code.configure(state=tk.DISABLED)

    def verifica(self, choice):
        if self.answered or self.current is None:
            return
        self.answered = True
        stats_tracker.record("async", choice == self.current["answer"])
        for b in self.option_buttons:
            b.config(state=tk.DISABLED)
            if b.cget("text") == self.current["answer"]:
                b.config(bg="#4CAF50")
            elif b.cget("text") == choice and choice != self.current["answer"]:
                b.config(bg="#F44336")
            else:
                b.config(bg="#9E9E9E")

        explain = self.t(self.current["explain_key"])
        if choice == self.current["answer"]:
            self.lbl_feedback.config(
                text=self.t("async_correct", ans=self.current["answer"], explain=explain),
                fg="#4CAF50",
            )
        else:
            self.lbl_feedback.config(
                text=self.t("async_wrong", ans=self.current["answer"], explain=explain),
                fg="#F44336",
            )


if __name__ == "__main__":
    root = tk.Tk()
    MainController(root)
    root.mainloop()

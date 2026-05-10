# DFS Simulator – Alberi Binari

Applicazione desktop in **Python + Tkinter** per esercitarsi con le visite in profondità (DFS) su alberi binari: **pre-order**, **in-order** e **post-order**.

L'app genera un albero binario casuale, propone una visita a sorte e chiede all'utente di scrivere la sequenza corretta dei nodi.

## Caratteristiche

- Generazione casuale di alberi binari (profondità configurabile da 2 a 8)
- Modalità "albero bilanciato" oppure casuale
- Tre tipi di visita DFS estratti a sorte: pre-order, in-order, post-order
- Suggerimento opzionale dell'ordine di visita (Radice / Sinistra / Destra)
- Verifica automatica della sequenza inserita
- Zoom in/out, reset, fit-to-view e pan trascinando il mouse
- Conteggio dei nodi visualizzato
- Interfaccia multilingua: italiano, inglese, spagnolo, francese, tedesco, portoghese

## Requisiti

- Python 3.8+
- Tkinter (incluso nelle distribuzioni standard di Python su Windows e macOS; su Linux può richiedere `python3-tk`)

Nessuna dipendenza esterna oltre alla libreria standard.

## Avvio

```bash
python array.py
```

## Utilizzo

1. Premi **🔄 Nuovo Albero** per generare un nuovo quiz.
2. Leggi la missione: ti verrà chiesta una visita pre-order, in-order o post-order.
3. Scrivi la sequenza dei valori nei nodi separati da spazi o virgole (es. `1 2 3 4` oppure `1,2,3,4`).
4. Premi **Verifica** o invio per controllare la risposta.

### Controlli del canvas

| Azione | Comando |
|---|---|
| Scroll verticale | Rotella del mouse |
| Zoom | `Ctrl` + rotella del mouse, oppure pulsanti 🔍+ / 🔍− |
| Pan | Click sinistro + trascinamento |
| Adatta alla finestra | Pulsante **Adatta** |
| Reset zoom | Pulsante **1:1** |

## Struttura del progetto

```
algo/
├── array.py        # Applicazione principale (UI + logica)
└── README.md
```

## Licenza

MIT

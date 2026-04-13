# VS Code Setup Guide — NUMA01

## 0. Klona repot (för Sixten / nya collaborators)

```bash
git clone https://github.com/Solsidan21/Ber-kningsprogrammering.git
cd Ber-kningsprogrammering
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Sedan följ steg 1-4 nedan.

---

## 1. Installera VS Code-extensions

Tryck Cmd+Shift+X och sök efter dessa:

- **Python** (`ms-python.python`)
- **Black Formatter** (`ms-python.black-formatter`)
- **Pylint** (`ms-python.pylint`)
- **Jupyter** (`ms-toolsai.jupyter`)

## 2. Välj rätt Python-interpreter

1. Cmd+Shift+P
2. Skriv "Python: Select Interpreter"
3. Välj `.venv/bin/python` (den virtuella miljön som redan är skapad)

## 3. Testa att allt fungerar

Öppna `scratch/playground.py` och tryck på triangelknappen (play-knapp) uppe till höger. En sinuskurva ska visas.

## 4. Spyder → VS Code snabbguide

| Vad du vill göra | Tryck |
|---|---|
| Kör hela filen | Triangelknappen eller Ctrl+F5 |
| Kör markerad kod | Markera + Shift+Enter |
| Skapa en "cell" | Skriv `# %%` i koden |
| Kör en cell | Shift+Enter |
| Kommandopalett | Cmd+Shift+P |
| Terminal | Cmd+` |

## 5. Studieordning inför Gruppuppgift 1

Deadline: **fredag 24 april 2026, kl 23:30**

### Dag 1-2: Python-grunder
- Läs `unit01_getting_started/lecture01.md`
- Gör training_assignment_1 (exercise01.pdf på Canvas)
- Fokus: for-loopar, if/else, importera numpy

### Dag 3-4: Listor och plotting
- Läs `unit02_containers_lists_dicts/lecture02.md`
- Läs `unit02_containers_lists_dicts/lecture03_summer.md`
- Gör training_assignment_2
- Fokus: **list comprehension**, matplotlib (`plot`, `xlabel`, `legend`, `show`), f-strings

### Dag 5-6: Funktioner
- Öppna `unit03_functions/lecture04.py` (kör med `# %%`-celler)
- Öppna `unit03_functions/lecture05.py`
- Gör exercise04 och exercise05
- Fokus: `def`-funktioner, docstrings, **rekurrensrelationer/iteration**, bisektionsmetoden

### Dag 7-10: Gruppuppgift 1 — "Approximating the Logarithm"
- Task 1: Skriv `approx_ln(x, n)` — aritmetisk-geometrisk medelvärdesiteration
- Task 2: Plotta ln vs approx_ln och differensen
- Task 3: Plotta absolutfelet vs n (för x = 1.41)
- Task 4: Skriv `fast_approx_ln(x, n)` — Richardson-extrapolation (svåraste)
- Task 5: Felplot med log-skala, iterationer 2-6
- Skriv tester och docstrings

### Dag 11: Förbered muntlig presentation med Sixten

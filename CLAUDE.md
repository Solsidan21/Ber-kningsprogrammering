# Projektinstruktioner — Beräkningsprogrammering (NUMA01)

## Kontext

Detta är kursmappen för NUMA01 Beräkningsprogrammering vid Lunds Universitet, VT2026.
Kursen följer boken *Scientific Computing with Python* av Führer, Solem & Verdier (2nd Ed., Packt 2021).

Studenter: Arvid Brenner & Sixten Midsem (gruppuppgifter görs ihop).

## Kursplanens progression

Kursen följer en bestämd ordning (Unit 01–09). Vid varje tillfälle har studenten bara gått igenom
en del av kursen. **Kontrollera vilka units som är avklarade** (se `README.md`-tabellen eller fråga
studenten) och anpassa lösningar därefter:

- Använd **bara koncept och verktyg från avklarade units** i lösningar och förklaringar
- Om en uppgift kräver koncept från en kommande unit: förklara konceptet från grunden och
  referera till relevant kapitel i kursboken så studenten kan läsa mer
- **Flagga tydligt** om en lösning använder något utöver det som täckts hittills

### Kursstruktur och progression
| Unit | Ämne | Kapitel i boken | Nyckelkoncept |
|------|------|-----------------|---------------|
| 01 | Getting Started | Kap 1 | Grundläggande Python, variabler, typer |
| 02 | Containers | Kap 2 | Listor, dictionaries, tuples |
| 03 | Functions | Kap 3, 7 | Funktioner, scope, lambda, rekursion, plotting (matplotlib) |
| 04 | Arrays & Linear Algebra | Kap 4–5 | NumPy arrays, vektorisering, linjär algebra |
| 05 | Classes & Exceptions | Kap 6, 8 | OOP, klasser, exceptions |
| 06 | File handling, Iterators | Kap 9 | Filhantering, iteratorer, generatorer |
| 07 | Plotting (matplotlib) | Kap 7 (fördjupning) | Avancerade plottar, GUI |
| 08 | Testing & Timing | Kap 10 | pytest, timing, profiling |
| 09 | Data handling (Pandas) | Kap 11 | pandas, dataframes |

## Kursbok-referens

Kursboken finns i `textbook/`. Om `textbook/textbook_content.md` finns, använd den som referens
för bokens kodstil, konventioner och notation istället för att öppna PDF:en direkt.

## Kodstil och konventioner

All kod i detta projekt ska följa kursbokens stil och konventioner:

### Python-version och paket
- Python 3.x
- Primära paket: **NumPy**, **SciPy**, **matplotlib**, **pandas**
- Testning: **pytest**
- Formatering: **black** (körs automatiskt vid spara i VS Code)

### Import-konventioner (följ kursboken)
```python
import numpy as np
from numpy import array, zeros, ones, linspace, arange
import scipy
import scipy.linalg as sl
import matplotlib.pyplot as plt
import pandas as pd
```

### Kodstil
- Använd **svenska** för kommentarer, docstrings och variabelnamn där det passar (t.ex. i övningar och anteckningar), men **engelska** för kod som ska vara generaliserbar
- Följ kursbokens notation: t.ex. `A` för matriser, `x`, `b` för vektorer
- Skriv **funktioner** snarare än skriptliknande kod när det är möjligt
- Kommentera vad koden gör, inte hur — fokusera på det matematiska/beräkningstekniska
- Använd `np.array` istället för Python-listor för numeriska beräkningar
- Använd vektoriserade operationer istället för loopar där NumPy stöder det

### Matematisk notation i kommentarer
- Referera till ekvationer och begrepp från kursboken där relevant
- Skriv matematisk notation i kommentarer: `# Löser Ax = b med LU-faktorisering`

### Filstruktur
- `exercises.py` — Övningar kopplade till respektive unit
- `training_assignment_X.py` — Tränningsuppgifter (bedöms ej)
- `notes.md` — Anteckningar från föreläsningar
- `lecture0X.py/.ipynb/.pdf` — Föreläsningsmaterial
- `homework/` — Inlämningsuppgifter (Arvid & Sixten ihop)
- `final_project/` — Slutprojekt (grupparbete)
- `scratch/playground.py` — Fritt experimenterande

### Testning
- Skriv enhetstester med `pytest` för homework och final_project
- Testerna läggs i samma mapp som koden, namngivna `test_*.py`

## IDE
VS Code med Python-extension, black-formatering och pylint.

## Pedagogiskt arbetssätt

Studenten ska kunna **redogöra för och förklara all kod muntligt** för sin lärare. Arbeta därför alltid pedagogiskt:

### Kursbok-referens vid uppgifter
- När studenten arbetar med övningar, homework eller final_project: **sök i `textbook/textbook_content.md`** efter relevanta avsnitt och begrepp
- Visa hur kursboken löser liknande problem och följ kursbokens approach som default
- Referera till specifika kapitel och avsnitt (t.ex. "Se avsnitt 4.9 — Linear algebra methods in SciPy")

### Alternativa lösningar
- Om det finns flera sätt att skriva koden: **visa kursbokens sätt först**
- Förklara sedan alternativ (t.ex. listcomp vs loop, vektoriserat vs iterativt, `scipy.linalg.solve` vs `numpy.linalg.solve`)
- Motivera vilken som är bäst och varför (prestanda, läsbarhet, kurskonvention)
- Markera tydligt om en lösning avviker från kursbokens rekommendation

### Muntlig redovisning-fokus
- Förklara **varför** koden fungerar, inte bara **vad** den gör
- Lyft fram nyckelbegrepp och terminologi som läraren förväntar sig (t.ex. "vektorisering", "broadcasting", "LU-faktorisering")
- Markera delar som troligen får följdfrågor (t.ex. "Varför vektoriserat istället för loop?" → prestanda + NumPy-idiom)
- Ge korta sammanfattningar av varje kodblock som studenten kan använda som muntlig förklaring

### Stegvis förståelse
- Vid komplex kod: bryt ner lösningen i logiska steg
- Förklara varje steg i relation till den matematiska/beräkningstekniska bakgrunden
- Koppla till relevanta kapitel i kursboken
- Använd konkreta exempel och mellanresultat för att visa vad som händer

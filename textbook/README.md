# Kursbok

**Scientific Computing with Python – High-Performance Scientific Computing with NumPy, SciPy, and pandas** (2nd Ed.)
Claus Führer, Jan Erik Solem, Olivier Verdier — Packt, 2021

## Filer

- `Scientific_Computing_with_Python_High-Performance_....pdf` — Original-PDF
- `textbook_content.md` — Extraherat textinnehåll (skapas med Claude Code, se nedan)

## Extrahera innehåll till Markdown

PDF:en är stor och bör inte läsas direkt av AI i varje konversation. Extrahera istället innehållet till en `.md`-fil med Claude Code i terminalen:

```bash
cd ~/Projects/Beräkningsprogrammering/textbook
claude "Läs PDF:en och extrahera allt textinnehåll till textbook_content.md, kapitel för kapitel med tydliga rubriker."
```

När `textbook_content.md` finns kan AI referera till den istället för att öppna PDF:en.

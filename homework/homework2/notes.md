# Homework 2 — Anteckningar och resonemang

Allt resonemang bakom `solution.ipynb` ligger här så själva inlämningen kan vara
ren kod. Använd det här dokumentet både som körschema inför försvaret och som
referens om en följdfråga dyker upp.

## Övergripande struktur

- **En enda klass `Interval`** med alla metoder definierade en gång. Vi använder
  *inte* en arvskedja `Interval1 → Interval2 → …` per task — det är inte bokens
  stil och tillför ett extra koncept (multipla nivåer av arv) som vi ändå inte
  utnyttjar.
- **Mönstret är taget direkt från kursbokens kap 8**, specifikt klasserna
  `RationalNumber` (kap 8.1) och `Function` (kap 8.5).
- **Kursbokens kap 8 övning 2** (rad 6442–6459 i `textbook_content.md`)
  beskriver *exakt* vår Homework 2-uppgift — inklusive `__contains__`,
  promotion av skalärer och polynom-applicering. Det är en stark referens
  vid försvar: "vi följer den övning boken själv definierar."

## Designval, rad för rad i klassen

### Konstruktorn (`__init__`)

```python
def __init__(self, a, b=None):
    self.a = a
    self.b = a if b is None else b
```

- **Varför `b=None` i stället för `b=a` som default?** Default-värden i Python
  evalueras vid funktionens *definition*, inte vid varje anrop, så `a` finns
  inte tillgängligt som default för `b`. Klassiskt nybörjarfel — vi hanterar
  det med "sentinel"-mönstret: `None` som markör + villkor inuti funktionen.
- **Varför inte två separata klasser för Task 1 och Task 7?** Boken visar
  aldrig det mönstret; samma konstruktor med en valfri parameter är
  vanligare och enklare.

### `__repr__`

```python
def __repr__(self):
    return f"[{self.a}, {self.b}]"
```

- Kap 8 rad 11721: *"It is always a good practice to define a `__repr__`
  method."*
- Boken behandlar inte `__str__` för vanliga klasser. När bara `__repr__`
  finns används den även av `print()` och `str()`, så ett enda format
  täcker allt.

### Skalär-promotion inuti varje operator

```python
if isinstance(other, (int, float)):
    other = type(self)(other)
```

- Bokens `RationalNumber.__add__` (rad 5779–5782) gör samma sak:
  ```python
  if isinstance(other, int):
      p2, q2 = other, 1
  else:
      p2, q2 = other.numerator, other.denominator
  ```
- **Avvikelse från boken:** vi accepterar `(int, float)`, boken bara `int`.
  Motivering: uppgift 8 testar `1.0` (float) explicit, så vi måste utöka.
- **Varför ingen separat hjälpare `_coerce`?** Boken visar det inline, och
  en extra metod gör att vi måste försvara två koncept i stället för ett.

### `type(self)(...)` när vi konstruerar resultat

- Kap 8 rad 6311–6312 (i `Function`-klassen): *"Note that the operations
  `__add__` and `__mul__` should return an instance of the same class.
  This is achieved by the statement `return type(self)(sum)`, which in
  this case is a more general form of writing `return Function(sum)`."*
- Försvar om frågan kommer: "Boken rekommenderar mönstret explicit för
  framtidssäkerhet vid arv. Vi har själva ingen subklass i denna
  inlämning, men följer bokens stil."

### Höger-versionerna delegerar tillbaka

```python
def __radd__(self, other):
    return self + other
```

- Bokens `RationalNumber.__radd__` (rad 5888–5889) ser exakt så ut.
- Bokens `Function.__radd__/__rmul__` (rad 6306–6309) likaså:
  ```python
  def __radd__(self, g):
      return self + g
  def __rmul__(self, g):
      return self * g
  ```
- **Varför inte `__radd__ = __add__` som kortform?** Två skäl:
  1. Boken gör det inte.
  2. Kortformen binder vid klassdefinition och bryter arvet om någon
     subklassar och overrider `__add__`.
- `__rsub__` är inte kommutativt, så där måste vi promota och vända
  ordningen: `type(self)(other) - self`.

### Multiplikation och division med "hörn-tricket"

```python
hörn = (a * c, a * d, b * c, b * d)
return type(self)(min(hörn), max(hörn))
```

- Argument: produkten (och kvoten) är bilinjär över rektangeln
  $[a, b] \times [c, d]$. En bilinjär funktion antar sina extremvärden
  på rektangelns hörn — alltså räcker det att räkna de fyra hörnvärdena
  och ta min/max.
- **Möjlig fråga:** "Kan ni bevisa det?" Snabbsvar: håller man ett intervall
  fast och varierar det andra blir funktionen linjär, och en linjär
  funktion antar extremvärden i ändpunkterna. Upprepa argumentet för
  den andra variabeln så ligger min/max alltid i ett hörn.

### Division med 0 i nämnaren

```python
if c <= 0 <= d:
    raise ZeroDivisionError(...)
```

- **Varför `ZeroDivisionError`?** Det är samma typ Python själv kastar för
  `1/0`. Idiomatiskt val: `try/except ZeroDivisionError` fångar både
  Pythons "vanliga" fall och vårt intervallfall.
- **Uppgiften nämner två fall:** "contains zero" och "infinitely large".
  Båda fångas av samma villkor `c <= 0 <= d`:
  - 0 är *ändpunkt* (c=0 eller d=0): division med exakt noll → odefinierad.
  - 0 *strikt inuti* (c<0<d): kvoten går mot ±∞ från båda sidor → obegränsad.
  Det är samma matematiska situation i två varianter, så ett villkor räcker.

### `__pow__` — udda och jämna fall

- Boken/uppgiften ger formlerna (1) och (2). Vår kod följer dem rakt av:
  - Udda → `[a^n, b^n]`.
  - Jämn, `a ≥ 0` → `[a^n, b^n]`.
  - Jämn, `b < 0` → `[b^n, a^n]` (vänd ändpunkterna).
  - Jämn, korsar 0 → `[0, max(a^n, b^n)]` (minsta värdet uppnås vid x=0).
- **Validering:** vi kollar `isinstance(n, int) and n >= 1` i början.
  Uppgiften specificerar `n ≥ 1`. Möjlig fråga: "Vad händer vid `I**0`
  eller `I**-1`?" Svar: vi kastar `ValueError` direkt.
- **Varför `I**2 ≠ I*I`?** Intervall-multiplikation behandlar de två
  faktorerna som *oberoende* variabler. Men i `I**2` är båda faktorerna
  samma `x` — sambandet förlorat ger ett bredare och felaktigt intervall.
  Exempel: `Interval(-2, 2) * Interval(-2, 2) = [-4, 4]`, medan
  `Interval(-2, 2) ** 2 = [0, 4]`.

### `__neg__`

```python
def __neg__(self):
    return type(self)(-self.b, -self.a)
```

- `-[a, b] = [-b, -a]` — ändpunkterna måste byta plats så att invarianten
  "vänster ≤ höger" upprätthålls.

## Task 10 — varför listcomp över zip?

- `[Interval(l, u) for l, u in zip(xl, xu)]` bygger 1000 intervall i en
  rad. Bokens kap 3 introducerar list comprehensions, så det är inom det
  som har gåtts igenom.
- **Alternativ:** vanlig for-loop med `.append()`. Ger samma resultat men
  längre kod.
- **Varför `xu = xl + 0.5` och inte `linspace(0., 1, 1000) + 0.5`?** Vi
  räknar `linspace` en gång; det är något snabbare och visar att vi
  utnyttjar NumPy-arrayens broadcasting.

## Försvarsfällor — vanliga följdfrågor och korta svar

| Fråga | Svar |
|-------|------|
| "Varför en klass, inte arvskedja per task?" | Boken visar inga sådana kedjor; alla exempel i kap 8 (RationalNumber, Function, Polynomial) är en huvudklass. |
| "Varför `type(self)(...)` om ni inte har en subklass?" | Boken rekommenderar mönstret explicit (rad 6311–6312). Framtidssäkert om vi senare hade ärvt. |
| "Varför `isinstance` inline, inte en hjälpare?" | Det är bokens exakta mönster (rad 5779–5782). En hjälpare hade tillfört ett extra koncept att försvara. |
| "Varför `ZeroDivisionError`, inte `ValueError`?" | Samma typ Python själv kastar för `1/0`. `try/except` blir enhetlig. |
| "Varför ett villkor i Task 6, när uppgiften nämner två fall?" | 0 i nämnaren *är* fallet med obegränsat resultat. Båda fall är samma matematiska situation. |
| "Validerar ni `n` i `__pow__`?" | Ja — `isinstance(n, int) and n >= 1`. Annars `ValueError`. |
| "Varför `__radd__ = self + other`?" | Bokens stil (rad 5888–5889, 6306–6309). Återanvänder logiken i vänsterversionen. |
| "Varför inte Task 11?" | Frivillig. Vektorisering av egen klass kräver `np.where`, subclassing och `np.minimum/maximum` — koncept som varken är i kap 8 eller har gåtts igenom på föreläsning än. |
| "Varför `I**2` i polynomet och inte `I*I`?" | Multiplikation tappar sambandet att samma `x` används i båda faktorer; `I*I` blir bredare än `I**2`. |
| "Varför `b=None` i konstruktorn, inte `b=a`?" | Default-värden binds vid funktionens definition, inte vid varje anrop — `a` är inte tillgängligt som default för `b`. |

## Sammanfattningstabell — koncept och bokreferenser

| Vad | Bokens stöd |
|-----|-------------|
| `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__pow__`, `__neg__` | Tabell 8.1 (rad 5805–5844) |
| `isinstance(other, (int, float))` inline | `RationalNumber.__add__` (rad 5779–5782) |
| `__radd__/__rsub__/__rmul__` delegerar | `RationalNumber.__radd__` (rad 5888–5889), `Function.__radd__/__rmul__` (rad 6306–6309) |
| `type(self)(...)` | `Function`-klassen (rad 6311–6312) |
| `__repr__` | Rad 11721 |
| `__contains__` | Kap 8 övning 2 (rad 6456–6457) |
| `ZeroDivisionError` | Inte i boken — Python-idiom (samma typ som `1/0`) |

## Vad vi medvetet inte gör

- **Task 11** (frivillig): hela vektoriseringsdelen ligger utanför kap 8 och
  utanför våra föreläsningar hittills.
- **`__pow__` med flyttalsexponenter**: uppgiften specificerar `n ≥ 1`,
  så vi behöver inte hantera det och vill inte introducera koncept som
  fraktionella potenser eller komplex aritmetik.
- **`__eq__`**: inte efterfrågat. Om vi lagt till det hade vi behövt
  bestämma "vad betyder lika?" (samma a och b? samma typ?) och försvara
  det valet. Hellre utelämna.
- **`__lt__`/`__gt__`**: intervall har ingen total ordning (vad är
  `[1, 5] < [3, 7]`?), så vi undviker att kasta in jämförelseoperatorer.

## Att göra innan inlämning

- [ ] Kör `Restart Kernel and Run All` så outputs i notebooken är färska.
- [ ] Läs igenom denna anteckning högt en gång var — Arvid och Sixten
      ska kunna alla rader i tabellen "Försvarsfällor" utantill.
- [ ] Verifiera att Task 4 och Task 8-utskrifterna i notebooken matchar
      exakt de värden uppgiften visar i sina kommentarer.
- [ ] Verifiera att Task 10-plotten har:
  - Blå undre kurva från ~−4 (x=0) till ~−10 (x=1)
  - Grön övre kurva från ~−1 (x=0) till ~2 (x=1)

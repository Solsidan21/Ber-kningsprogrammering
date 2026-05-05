# Homework 2 — Interval Analysis
# Arvid Brenner & Sixten Midsem, NUMA01 VT2026

# Bokens kap 1.1.4 rekommenderar wildcard-import — då får vi linspace, plot osv direkt
from numpy import *
from matplotlib.pyplot import *

# Vi bygger upp Interval-klassen task för task med arv (Unit 05).
# Varje subklass lägger till eller skriver om det som just den tasken kräver.
# Längst ner aliasar vi Interval = Interval9 så det blir den användbara klassen.


# --- Task 1: konstruktor med två argument ---

class Interval1:
    """Task 1: ett intervall [a, b] initierat med två reella tal."""

    def __init__(self, left, right):
        self.left = left      # vänster ändpunkt a
        self.right = right    # höger ändpunkt b


# --- Task 2: de fyra grundoperationerna (Interval mot Interval) ---

class Interval2(Interval1):
    """Task 2: +, -, *, / mellan två intervaller."""

    def __add__(self, other):
        # [a,b] + [c,d] = [a+c, b+d]
        # type(self) gör att resultatet får samma klass som self (viktigt när vi ärver)
        return type(self)(self.left + other.left, self.right + other.right)

    def __sub__(self, other):
        # [a,b] - [c,d] = [a-d, b-c] — minsta minus största, största minus minsta
        return type(self)(self.left - other.right, self.right - other.left)

    def __mul__(self, other):
        a, b = self.left, self.right
        c, d = other.left, other.right
        # alla fyra hörnprodukter — minsta och största blir nya ändpunkterna
        produkter = [a * c, a * d, b * c, b * d]
        return type(self)(min(produkter), max(produkter))

    def __truediv__(self, other):
        a, b = self.left, self.right
        c, d = other.left, other.right
        # samma princip som multiplikation: kolla alla fyra hörnkvoter
        # (felhantering kommer i task 6, här antar vi att 0 inte finns i [c, d])
        kvoter = [a / c, a / d, b / c, b / d]
        return type(self)(min(kvoter), max(kvoter))


# --- Task 3: textrepresentation [a, b] ---

class Interval3(Interval2):
    """Task 3: print(I) ska skriva [a, b]."""

    def __repr__(self):
        return f"[{self.left}, {self.right}]"


# Task 4 är en ren verifiering — ingen ny klass behövs.
# Demo-anropen ligger längst ned i if __name__ == "__main__".


# --- Task 5: medlemskapstest (x in I) ---

class Interval5(Interval3):
    """Task 5: x in Interval(a, b) ska vara True om a ≤ x ≤ b."""

    def __contains__(self, x):
        # inklusive ändpunkterna enligt uppgiftens definition
        return self.left <= x <= self.right


# --- Task 6: division med felhantering ---

class Interval6(Interval5):
    """Task 6: utöka __truediv__ så den kastar fel vid 0 i nämnaren."""

    def __truediv__(self, other):
        c, d = other.left, other.right
        # 0 i nämnar-intervallet ger antingen division med noll eller oändligt brett resultat
        if c <= 0 <= d:
            raise ValueError("Division med intervall som innehåller 0 är inte tillåten")
        # om felkollen passerar, gör samma uträkning som i task 2
        return super().__truediv__(other)


# --- Task 7: degenererat intervall (en-arg-konstruktor) ---

class Interval7(Interval6):
    """Task 7: Interval(r) ska tolkas som [r, r]."""

    def __init__(self, left, right=None):
        # om bara ett tal ges blir det ett degenererat intervall [r, r]
        if right is None:
            right = left
        # låt task 1:s __init__ sköta själva tilldelningen via super()
        super().__init__(left, right)


# --- Task 8: blandade Interval-skalär-operationer + unär negation ---

class Interval8(Interval7):
    """Task 8: stöd för Interval +/-/* tal (åt båda håll) samt -Interval."""

    def __add__(self, other):
        # om other är ett tal, gör om det till degenererat intervall
        if isinstance(other, (int, float)):
            other = type(self)(other)
        # och låt sedan task 2:s __add__ göra själva räkningen
        return super().__add__(other)

    def __radd__(self, other):
        # tal + intervall — addition är kommutativ, så återanvänd __add__
        return self + other

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = type(self)(other)
        return super().__sub__(other)

    def __rsub__(self, other):
        # tal - intervall — ej kommutativt, så vi byter ordning
        if isinstance(other, (int, float)):
            other = type(self)(other)
        return other - self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = type(self)(other)
        return super().__mul__(other)

    def __rmul__(self, other):
        # multiplikation är kommutativ
        return self * other

    def __neg__(self):
        # -[a, b] = [-b, -a] — vi måste vända ändpunkterna så vänster ≤ höger
        return type(self)(-self.right, -self.left)


# --- Task 9: potens (x ↦ x^n) ---

class Interval9(Interval8):
    """Task 9: I**n med särskild hantering av udda och jämna n."""

    def __pow__(self, n):
        a, b = self.left, self.right
        # udda exponent: x^n är monotont stigande, ändpunkterna mappas direkt
        if n % 2 == 1:
            return type(self)(a ** n, b ** n)
        # jämn exponent — tre fall beroende på var intervallet ligger
        if a >= 0:
            # icke-negativt intervall — x^n monotont stigande här
            return type(self)(a ** n, b ** n)
        if b < 0:
            # helt negativt — x^n monotont avtagande, vänd ändpunkterna
            return type(self)(b ** n, a ** n)
        # 0 ligger inuti [a, b] — minsta värdet är 0, största är max av ändpunkts-potenserna
        # OBS: vi använder max([..]) på en lista. max(x, y) på två skalärer fungerar inte
        # eftersom from numpy import * skuggar Pythons max (numpy tolkar arg2 som axis)
        return type(self)(0, max([a ** n, b ** n]))


# Slutlig, användbar klass — den vi instansierar i task 10
Interval = Interval9


# === Verifiering av varje task + task 10 ===

if __name__ == "__main__":

    # --- Task 4: verifiera att grundoperationerna ger förväntade resultat ---
    print("Task 4 — grundoperationer:")
    I1 = Interval(1, 4)         # [1, 4]
    I2 = Interval(-2, -1)       # [-2, -1]
    print("  I1 + I2 =", I1 + I2)   # förväntat [-1, 3]
    print("  I1 - I2 =", I1 - I2)   # förväntat [2, 6]
    print("  I1 * I2 =", I1 * I2)   # förväntat [-8, -1]
    print("  I1 / I2 =", I1 / I2)   # förväntat [-4.0, -0.5]

    # --- Task 5: medlemskap ---
    print("\nTask 5 — medlemskap:")
    print("  3 in [1, 5]?", 3 in Interval(1, 5))     # True
    print("  6 in [1, 5]?", 6 in Interval(1, 5))     # False

    # --- Task 6: division med 0 i nämnaren ska kasta fel ---
    print("\nTask 6 — division med 0 i nämnaren:")
    try:
        Interval(1, 2) / Interval(-1, 1)
    except ValueError as e:
        print("  ValueError fångat:", e)

    # --- Task 7: degenererat intervall ---
    print("\nTask 7 — degenererat intervall:")
    print("  Interval(1) =", Interval(1))   # [1, 1]

    # --- Task 8: blandade Interval-skalär-operationer ---
    print("\nTask 8 — Interval och skalär:")
    print("  Interval(2, 3) + 1   =", Interval(2, 3) + 1)     # [3, 4]
    print("  1 + Interval(2, 3)   =", 1 + Interval(2, 3))     # [3, 4]
    print("  1.0 + Interval(2, 3) =", 1.0 + Interval(2, 3))   # [3.0, 4.0]
    print("  Interval(2, 3) + 1.0 =", Interval(2, 3) + 1.0)   # [3.0, 4.0]
    print("  1 - Interval(2, 3)   =", 1 - Interval(2, 3))     # [-2, -1]
    print("  Interval(2, 3) - 1   =", Interval(2, 3) - 1)     # [1, 2]
    print("  1.0 - Interval(2, 3) =", 1.0 - Interval(2, 3))   # [-2.0, -1.0]
    print("  Interval(2, 3) - 1.0 =", Interval(2, 3) - 1.0)   # [1.0, 2.0]
    print("  Interval(2, 3) * 1   =", Interval(2, 3) * 1)     # [2, 3]
    print("  1 * Interval(2, 3)   =", 1 * Interval(2, 3))     # [2, 3]
    print("  1.0 * Interval(2, 3) =", 1.0 * Interval(2, 3))   # [2.0, 3.0]
    print("  Interval(2, 3) * 1.0 =", Interval(2, 3) * 1.0)   # [2.0, 3.0]
    print("  -Interval(4, 5)      =", -Interval(4, 5))        # [-5, -4]

    # --- Task 9: potens ---
    print("\nTask 9 — potens:")
    x = Interval(-2, 2)
    print("  Interval(-2, 2)**2 =", x ** 2)   # förväntat [0, 4]
    print("  Interval(-2, 2)**3 =", x ** 3)   # förväntat [-8, 8]

    # --- Task 10: 1000 intervaller, polynom, plot ---

    # vänster- och högerändar — högerändarna är förskjutna 0.5 enligt uppgiften
    xl = linspace(0., 1, 1000)
    xu = linspace(0., 1, 1000) + 0.5

    # bygg listan av intervaller med listcomp och zip
    intervaller = [Interval(l, u) for l, u in zip(xl, xu)]

    # polynomet p(I) = 3I^3 - 2I^2 - 5I - 1 — alla operatorer är redan implementerade
    p = lambda I: 3 * I ** 3 - 2 * I ** 2 - 5 * I - 1

    # utvärdera p på varje intervall — resultatet är en lista av Interval-objekt
    resultat = [p(I) for I in intervaller]

    # plocka ut nedre och övre gränserna ur varje resultatintervall
    yl = [r.left for r in resultat]
    yu = [r.right for r in resultat]

    # rita upp båda kurvorna i samma plot enligt uppgiftsbilden
    plot(xl, yl, "b", label="nedre gräns")
    plot(xl, yu, "g", label="övre gräns")
    title("p(I) = 3I^3 − 2I^2 − 5I − 1, I = Interval(x, x+0.5)")
    xlabel("x")
    ylabel("p(I)")
    legend()
    show()

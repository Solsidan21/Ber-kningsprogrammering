# Playground – snabba experiment och test
# Kör den här filen för att verifiera att miljön är korrekt uppsatt

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
plt.plot(x, np.sin(x), label="sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Setup test – om du ser denna plot fungerar allt!")
plt.legend()
plt.show()

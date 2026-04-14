# Homework 1 — Approximating the Logarithm
# NUMA01 Beräkningsprogrammering, VT2026
# Arvid Brenner & Sixten Midsem

import numpy as np
from numpy import sqrt, log, zeros, linspace
import matplotlib.pyplot as plt


# --- Task 1 ---

def approx_ln(x, n):
    """Approximerar ln(x) med Carlsons AGM-iteration.

    Metoden bygger på att beräkna aritmetiskt och geometriskt medelvärde
    iterativt. Efter n steg approximeras ln(x) som (x - 1) / a_n.

    Parametrar:
        x : float eller array — värde(n) att beräkna ln för (x > 0)
        n : int — antal iterationssteg

    Returnerar:
        float eller array — approximation av ln(x)
    """
    x = np.asarray(x, dtype=float)
    a = (1 + x) / 2
    g = sqrt(x)

    for _ in range(n):
        a, g = (a + g) / 2, sqrt((a + g) / 2 * g)

    return (x - 1) / a


# --- Task 4: Hjälpfunktion ---

def _compute_a_values(x, n):
    """Beräknar alla a_0, a_1, ..., a_n från AGM-iterationen.

    Returnerar en array med n+1 element.
    Endast skalär input.
    """
    a_vals = zeros(n + 1)
    a = (1 + x) / 2
    g = sqrt(x)
    a_vals[0] = a

    for i in range(n):
        a = (a + g) / 2
        g = sqrt(a * g)
        a_vals[i + 1] = a

    return a_vals


# --- Task 4 ---

def fast_approx_ln(x, n):
    """Approximerar ln(x) med Carlsons metod + Richardson-extrapolation.

    Richardson-extrapolation accelererar konvergensen genom att
    eliminera lägre ordningens feltermer. Tabellen d[k, i] byggs upp
    enligt:
        d[0, i] = a_i
        d[k, i] = (d[k-1, i] - 4^(-k) * d[k-1, i-1]) / (1 - 4^(-k))

    Approximationen ges av (x - 1) / d[n, n].

    Parametrar:
        x : float — värde att beräkna ln för (x > 0)
        n : int — antal iterationssteg / extrapolationsnivåer

    Returnerar:
        float — approximation av ln(x)
    """
    a_vals = _compute_a_values(x, n)

    # Bygg Richardson-tabellen
    d = zeros((n + 1, n + 1))
    for i in range(n + 1):
        d[0, i] = a_vals[i]

    for i in range(1, n + 1):
        for k in range(1, i + 1):
            d[k, i] = (d[k-1, i] - 4**(-k) * d[k-1, i-1]) / (1 - 4**(-k))

    return (x - 1) / d[n, n]


# --- Task 2 ---

def plot_comparison():
    """Plottar ln(x) vs approx_ln(x, n) och deras differens."""
    x = linspace(0.01, 5, 200)
    n_values = [1, 2, 3, 5]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Vänster: funktionerna
    ax1.plot(x, log(x), 'k-', linewidth=2, label='ln(x)')
    for n in n_values:
        ax1.plot(x, approx_ln(x, n), '--', label=f'approx_ln(x, {n})')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('ln(x) och approx_ln(x, n)')
    ax1.legend()
    ax1.grid(True)

    # Höger: differensen
    for n in n_values:
        ax2.plot(x, approx_ln(x, n) - log(x), label=f'n = {n}')
    ax2.set_xlabel('x')
    ax2.set_ylabel('approx_ln(x, n) - ln(x)')
    ax2.set_title('Differens mellan approx_ln och ln')
    ax2.legend()
    ax2.grid(True)

    fig.tight_layout()


# --- Task 3 ---

def plot_error_convergence():
    """Plottar |fel| vs n för x = 1.41."""
    x = 1.41
    n_values = range(0, 16)
    errors = [abs(approx_ln(x, n) - log(x)) for n in n_values]

    plt.figure()
    plt.semilogy(list(n_values), errors, 'o-')
    plt.xlabel('n (antal iterationer)')
    plt.ylabel('|approx_ln(1.41, n) - ln(1.41)|')
    plt.title('Felkonvergens för approx_ln, x = 1.41')
    plt.grid(True)


# --- Task 5 ---

def plot_fast_convergence():
    """Plottar felet för fast_approx_ln för iterationer 2-6."""
    x_values = linspace(0.01, 20, 300)
    n_values = [2, 3, 4, 5, 6]

    # Vektorisera fast_approx_ln för array-input
    fast_ln_vec = np.vectorize(fast_approx_ln)

    plt.figure()
    for n in n_values:
        errors = abs(fast_ln_vec(x_values, n) - log(x_values))
        plt.semilogy(x_values, errors, label=f'n = {n}')

    plt.xlabel('x')
    plt.ylabel('|fel|')
    plt.title('Error behavior of the accelerated Carlson method for the log')
    plt.legend()
    plt.grid(True)


if __name__ == "__main__":
    plot_comparison()
    plot_error_convergence()
    plot_fast_convergence()
    plt.show()

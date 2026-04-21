# Homework 1 — Approximating the Logarithm
# NUMA01 Beräkningsprogrammering, VT2026
# Arvid Brenner & Sixten Midsem

import numpy as np
from numpy import sqrt, log, zeros, linspace
import matplotlib.pyplot as plt


# --- Task 1 ---

def approx_ln(x, n):
    """Approximate ln(x) with Carlson's AGM iteration after n steps.

    Works for both scalar and array input (x > 0).
    """
    x = np.asarray(x, dtype=float)
    a = (1 + x) / 2
    g = sqrt(x)

    for _ in range(n):
        a, g = (a + g) / 2, sqrt((a + g) / 2 * g)

    return (x - 1) / a


# --- Task 2 ---

def plot_comparison():
    """Plot ln(x) and approx_ln(x, n) for n = 1, 2, 3, 5 and their difference."""
    x = linspace(0.01, 5, 200)
    n_values = [1, 2, 3, 5]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Left: the functions
    ax1.plot(x, log(x), 'k-', linewidth=2, label='ln(x)')
    for n in n_values:
        ax1.plot(x, approx_ln(x, n), '--', label=f'approx_ln(x, {n})')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('ln(x) and approx_ln(x, n)')
    ax1.legend()
    ax1.grid(True)

    # Right: the difference
    for n in n_values:
        ax2.plot(x, approx_ln(x, n) - log(x), label=f'n = {n}')
    ax2.set_xlabel('x')
    ax2.set_ylabel('approx_ln(x, n) - ln(x)')
    ax2.set_title('Difference between approx_ln and ln')
    ax2.legend()
    ax2.grid(True)

    fig.tight_layout()


# --- Task 3 ---

def plot_error_convergence():
    """Plot |approx_ln(1.41, n) - ln(1.41)| on a log scale for n = 0..15."""
    x = 1.41
    n_values = range(0, 16)
    errors = [abs(approx_ln(x, n) - log(x)) for n in n_values]

    plt.figure()
    plt.semilogy(list(n_values), errors, 'o-')
    plt.xlabel('n (number of iterations)')
    plt.ylabel('|approx_ln(1.41, n) - ln(1.41)|')
    plt.title('Error convergence for approx_ln, x = 1.41')
    plt.grid(True)


# --- Task 4: helper ---

def _compute_a_values(x, n):
    """Return all a_0, ..., a_n from the AGM iteration (scalar x only)."""
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
    """Approximate ln(x) with Carlson's method + Richardson extrapolation.

    Builds a table d[k, i] that eliminates error terms of order 4^(-k).
    """
    a_vals = _compute_a_values(x, n)

    # Build the Richardson table
    d = zeros((n + 1, n + 1))
    for i in range(n + 1):
        d[0, i] = a_vals[i]

    for i in range(1, n + 1):
        for k in range(1, i + 1):
            d[k, i] = (d[k-1, i] - 4**(-k) * d[k-1, i-1]) / (1 - 4**(-k))

    return (x - 1) / d[n, n]


# --- Task 5 ---

def plot_fast_convergence():
    """Plot |fast_approx_ln(x, n) - ln(x)| on a log scale for n = 2..6."""
    x_values = linspace(0.01, 20, 300)
    n_values = [2, 3, 4, 5, 6]

    # Vectorize fast_approx_ln for array input
    fast_ln_vec = np.vectorize(fast_approx_ln)

    plt.figure()
    for n in n_values:
        errors = abs(fast_ln_vec(x_values, n) - log(x_values))
        plt.semilogy(x_values, errors, label=f'n = {n}')

    plt.xlabel('x')
    plt.ylabel('|error|')
    plt.title('Error behavior of the accelerated Carlson method for the log')
    plt.legend()
    plt.grid(True)


if __name__ == "__main__":
    plot_comparison()
    plot_error_convergence()
    plot_fast_convergence()
    plt.show()

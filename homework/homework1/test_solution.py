"""Tester för Homework 1 — Approximating the Logarithm."""

import numpy as np
import pytest
from numpy import log
from solution import approx_ln, fast_approx_ln


# --- Tester för approx_ln ---

class TestApproxLn:
    def test_ln_of_one(self):
        """ln(1) = 0, och (1-1)/a = 0 exakt för alla n."""
        for n in range(6):
            assert approx_ln(1.0, n) == 0.0

    def test_zero_iterations(self):
        """Med n=0 returneras (x-1) / a_0 = 2(x-1)/(1+x)."""
        x = 3.0
        expected = 2 * (x - 1) / (1 + x)
        np.testing.assert_allclose(approx_ln(x, 0), expected)

    def test_convergence(self):
        """Felet ska minska med ökande n."""
        x = 2.0
        errors = [abs(approx_ln(x, n) - log(x)) for n in range(10)]
        for i in range(1, len(errors)):
            assert errors[i] <= errors[i - 1]

    def test_accuracy_high_n(self):
        """Med tillräckligt många iterationer ska vi vara nära ln(x)."""
        x = 2.0
        np.testing.assert_allclose(approx_ln(x, 10), log(x), atol=1e-10)

    def test_array_input(self):
        """Funktionen ska hantera array-input."""
        x = np.array([0.5, 1.0, 2.0, 5.0])
        result = approx_ln(x, 8)
        np.testing.assert_allclose(result, log(x), atol=1e-4)

    @pytest.mark.parametrize("x", [0.1, 0.5, 1.0, 1.41, 2.0, 5.0, 10.0])
    def test_various_x(self, x):
        """Testar noggrannhet för flera x-värden."""
        np.testing.assert_allclose(approx_ln(x, 12), log(x), atol=1e-8)


# --- Tester för fast_approx_ln ---

class TestFastApproxLn:
    def test_ln_of_one(self):
        """ln(1) = 0, exakt för alla n."""
        for n in range(6):
            assert fast_approx_ln(1.0, n) == 0.0

    def test_better_than_basic(self):
        """Richardson-extrapolation ska ge bättre resultat för samma n."""
        x = 2.0
        for n in range(2, 6):
            err_basic = abs(approx_ln(x, n) - log(x))
            err_fast = abs(fast_approx_ln(x, n) - log(x))
            assert err_fast <= err_basic

    def test_accuracy(self):
        """Med n=4 ska fast_approx_ln vara mycket nära ln(x)."""
        x = 2.0
        np.testing.assert_allclose(fast_approx_ln(x, 4), log(x), atol=1e-14)

    def test_n_zero_same_as_basic(self):
        """Med n=0 ska båda metoderna ge samma resultat."""
        x = 3.0
        np.testing.assert_allclose(
            fast_approx_ln(x, 0), approx_ln(x, 0), atol=1e-15
        )

    @pytest.mark.parametrize("x", [0.1, 0.5, 1.41, 2.0, 5.0, 10.0])
    def test_various_x(self, x):
        """Testar noggrannhet för flera x-värden med n=5."""
        np.testing.assert_allclose(fast_approx_ln(x, 5), log(x), atol=1e-12)

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fractions import Fraction
import pytest

from src.padic import valuation_p, valuation_p_fraction, is_p_integral

def test_valuation_basic():
    assert valuation_p(12, 2) == 2
    assert valuation_p(12, 3) == 1
    assert valuation_p(8, 2) == 3
    assert valuation_p(7, 2) == 0
    assert valuation_p(100, 5) == 2
    assert valuation_p(1, 2) == 0

def test_valuation_zero_raises():
    with pytest.raises(ValueError):
        valuation_p(0, 2)

def test_fraction_valuation():
    assert valuation_p_fraction(Fraction(12, 8), 2) == -1
    assert valuation_p_fraction(Fraction(7, 9), 2) == 0

def test_two_integrality_of_um():
    """Qualitative Lemma 5.4 check: u_m is 2-integral (odd denominators)."""
    from src.weighted import u_m_truncated

    for m in range(21):
        u = u_m_truncated(m, N=200)
        assert is_p_integral(u, 2), f"u_{m} is not 2-integral"
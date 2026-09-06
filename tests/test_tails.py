import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fractions import Fraction
from src.tails import T_m_truncated, verify_recurrence_exact, recurrence_residual

def test_recurrence_exact_range():
    """eq (1.3) as exact finite telescoping, m=0..50, N=100."""
    for m in range(51):
        res = verify_recurrence_exact(m, N=100)
        assert res["exact_match"], (
            f"FAIL at m={m}: diff={res['diff']}, "
            f"expected={res['expected_residual']}"
        )

def test_recurrence_residual_form():
    """Residual has the closed telescoping form."""
    for m in (0, 3, 17):
        for N in (1, 2, 5, 50):
            r = recurrence_residual(m, N)
            sign = 1 if (N - 1) % 2 == 0 else -1
            assert r == Fraction(sign, (2 * m + 2 * N + 1) ** 2)

def test_tail_exact_type():
    """All tail computations are exact Fractions."""
    t = T_m_truncated(4, 20)
    assert isinstance(t, Fraction)
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fractions import Fraction
from src.weighted import u_m_truncated, verify_weighted_consistency

def test_weighted_consistency_range():
    """eq (1.2): (2m+1)*u_m == T_m for m=0..20."""
    for m in range(21):
        assert verify_weighted_consistency(m, N=100)

def test_weighted_exact_type():
    u = u_m_truncated(2, 15)
    assert isinstance(u, Fraction)
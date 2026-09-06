"""Weighted tail u_m.

Paper eq (1.2):  u_m = T_m / (2m+1)

Confirmed traceable to the original paper.
"""

from fractions import Fraction

from .tails import T_m_truncated

def u_m_truncated(m: int, N: int) -> Fraction:
    """Truncated weighted tail u_m^{(N)} = T_m^{(N)} / (2m+1)."""
    return T_m_truncated(m, N) / Fraction(2 * m + 1)

def verify_weighted_consistency(m: int, N: int) -> bool:
    """Check (2m+1)*u_m == T_m exactly (implementation self-check)."""
    return (2 * m + 1) * u_m_truncated(m, N) == T_m_truncated(m, N)
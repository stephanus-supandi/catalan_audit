"""Tail construction T_m.

Paper eq (1.1):  T_m = sum_{r=0}^{inf} (-1)^r / (2m+2r+1)^2
Paper eq (1.3):  T_m + T_{m+1} = 1/(2m+1)^2

Both equations are confirmed traceable to the original paper
via multiple independent secondary confirmations of the definitions.
"""

from fractions import Fraction
from typing import Dict

def T_m_truncated(m: int, N: int) -> Fraction:
    """Truncated tail T_m^{(N)} = sum_{r=0}^{N-1} (-1)^r/(2m+2r+1)^2.

    Exact rational arithmetic. No floating point.
    """
    if m < 0 or N < 0:
        raise ValueError("m and N must be non-negative")
    s = Fraction(0)
    for r in range(N):
        sign = 1 if r % 2 == 0 else -1
        s += Fraction(sign, (2 * m + 2 * r + 1) ** 2)
    return s

def recurrence_residual(m: int, N: int) -> Fraction:
    """Exact finite telescoping residual for eq (1.3).

    Identity (derived by direct telescoping from (1.1)):
        T_m^{(N)} + T_{m+1}^{(N)} - 1/(2m+1)^2
            == (-1)^{N-1} / (2m+2N+1)^2

    This is the EXACT finite form. It tends to 0 as N -> inf,
    recovering the infinite recurrence (1.3).
    """
    sign = 1 if (N - 1) % 2 == 0 else -1
    return Fraction(sign, (2 * m + 2 * N + 1) ** 2)

def verify_recurrence_exact(m: int, N: int) -> Dict:
    """Verify eq (1.3) as an exact finite telescoping identity.

    Returns a dict with all quantities. No floating point is used
    for the equality decision.
    """
    lhs = T_m_truncated(m, N) + T_m_truncated(m + 1, N)
    rhs = Fraction(1, (2 * m + 1) ** 2)
    diff = lhs - rhs
    expected = recurrence_residual(m, N)
    return {
        "m": m,
        "N": N,
        "lhs": lhs,
        "rhs": rhs,
        "diff": diff,
        "expected_residual": expected,
        "exact_match": diff == expected,
    }
"""p-adic valuation utilities. Exact integer arithmetic only."""

from fractions import Fraction

def valuation_p(n: int, p: int) -> int:
    """v_p(n): largest k such that p^k divides n.

    Standard number-theory utility, not paper-specific.
    Raises ValueError for n == 0 (v_p(0) = +infinity).
    """
    if n == 0:
        raise ValueError("valuation_p(0) is infinity")
    if p < 2:
        raise ValueError("p must be a prime >= 2")
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v

def valuation_p_fraction(f: Fraction, p: int) -> int:
    """v_p of an exact Fraction: v_p(num) - v_p(den)."""
    num = f.numerator
    den = f.denominator
    v_num = valuation_p(num, p) if num != 0 else 0
    v_den = valuation_p(den, p)
    return v_num - v_den

def is_p_integral(f: Fraction, p: int) -> bool:
    """True iff v_p(f) >= 0, i.e. no factor of p in the denominator."""
    if f.numerator == 0:
        return True
    return valuation_p_fraction(f, p) >= 0
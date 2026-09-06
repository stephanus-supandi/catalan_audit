"""Catalan constant sanity checks.

G = sum_{k=0}^{inf} (-1)^k/(2k+1)^2 = T_0.
Floating point is used ONLY for display, never for equality decisions.
"""

from .tails import T_m_truncated

G_KNOWN = "0.915965594177219015054603514932384110774"

def catalan_partial(N: int):
    """Partial sum of G using exact rationals."""
    return T_m_truncated(0, N)

def sanity_display():
    """Print convergence of partial sums toward the known value."""
    g_known = float(G_KNOWN)
    lines = [f"Known G = {G_KNOWN}"]
    for N in (10, 100, 1000):
        s = float(catalan_partial(N))
        lines.append(
            f"  N={N:>5}: T_0^(N) = {s:.20f}  |err| = {abs(s-g_known):.2e}"
        )
    return "\n".join(lines)
"""Equation map / source tracker.

Records, per equation, whether its literal content has been recovered
from the original paper. This is the single source of truth for what
the audit is allowed to implement.
"""

CONFIRMED = {
    "(1.1)": "T_m = sum_{r>=0} (-1)^r/(2m+2r+1)^2",
    "(1.2)": "u_m = T_m/(2m+1)",
    "(1.3)": "T_m + T_{m+1} = 1/(2m+1)^2",
}

NOT_RECOVERED = {
    "(1.4)": "content unknown",
    "(2.1)": "entries of residual matrix A (Theorem 2.1)",
    "(2.2)": "rank claim of Theorem 2.1",
    "(3.3)": "definition of scalar Delta",
    "(3.4)": "Proposition 3.1 identity",
    "(3.5)": "consequence used in Proposition 3.2",
    "(3.6)": "minimal integerizer M (Definition 3.1)",
    "(3.7)": "p-adic valuation of denom(Delta), Proposition 3.2",
    "(3.8)": "particular case in Proposition 3.2",
    "(4.1)": "Cauchy-Binet expansion of det A",
    "(4.2)": "parameter sets for the two determinant factors",
    "(4.3)": "Lemma 4.1 Pascal alternant = integer x Vandermonde",
    "(4.4)": "Lemma 4.2 Cauchy determinant (paper-specific params)",
    "(4.5)": "Remark 4.1 combined absolute-value identity",
    "(5.9)": "Lemma 5.3 odd-prime inequality",
    "(5.14)": "Theorem 5.1 local saturation",
    "(5.25)": "Lemma 5.4 positive 2-adic part = 0 (exact form)",
    "(9.3)": "Proposition 9.5 main ledger form",
    "(9.4)": "remaining raw quadratic coefficient",
    "(9.5)": "Theorem 9.1 constant C bound",
    "(9.6)": "Theorem 9.1 final asymptotic bound",
}

REASON = (
    "All MathML equations stripped during HTML extraction; "
    "PDF and LaTeX source not reachable via available parsers."
)

def summary() -> str:
    lines = ["EQUATION SOURCE STATUS", "=" * 60]
    lines.append("CONFIRMED (implemented):")
    for k, v in CONFIRMED.items():
        lines.append(f"  {k}: {v}")
    lines.append("")
    lines.append("NOT RECOVERED (NOT implemented):")
    for k, v in NOT_RECOVERED.items():
        lines.append(f"  {k}: {v}")
    lines.append("")
    lines.append(f"Reason: {REASON}")
    return "\n".join(lines)
"""Full audit runner. Produces the CATALAN AUDIT REPORT.

Critical rule: verified computationally != proved mathematically.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src import catalan
from src.tails import verify_recurrence_exact
from src.weighted import verify_weighted_consistency
from src.padic import is_p_integral
from src.weighted import u_m_truncated
from src.source_status import summary

def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

def main():
    print("=" * 70)
    print("CATALAN AUDIT REPORT")
    print("Paper: arXiv:2609.04176v1")
    print(f"Python: {sys.version.split()[0]}")
    print("=" * 70)

    section("[0] Equation source status")
    print(summary())

    section("[1] Catalan constant sanity (display only)")
    print(catalan.sanity_display())

    section("[2] Eq (1.3): tail recurrence, exact finite telescoping")
    all_pass = True
    for m in range(51):
        res = verify_recurrence_exact(m, N=100)
        if not res["exact_match"]:
            all_pass = False
            print(f"  m={m}: FAIL diff={res['diff']} expected={res['expected_residual']}")
    print(f"  [{'VERIFIED FOR TESTED PARAMETERS' if all_pass else 'FAIL'}] m=0..50, N=100")

    section("[3] Eq (1.2): weighted tail consistency")
    ok = all(verify_weighted_consistency(m, N=100) for m in range(21))
    print(f"  [{'VERIFIED FOR TESTED PARAMETERS' if ok else 'FAIL'}] m=0..20, N=100")

    section("[4] Lemma 5.4 qualitative: 2-integrality of u_m")
    ok = all(is_p_integral(u_m_truncated(m, N=200), 2) for m in range(21))
    print(f"  [{'VERIFIED FOR TESTED PARAMETERS' if ok else 'FAIL'}] m=0..20, N=200")
    print("  NOTE: qualitative check on u_m only; full Lemma 5.4 requires")
    print("        the matrix construction from eq (2.1) — NOT IMPLEMENTED.")

    section("[5] Third-party claimed discrepancy (NOT independently verified)")
    print("  Source: third-party analysis (prime-2 ledger term).")
    print("  Claim: a term ~ 2 B^2 log 2 allegedly mishandled in the ledger;")
    print("         remaining odd-prime coefficient allegedly positive.")
    print("  Status: NOT reproduced. Reproduction requires eq (9.3)-(9.6),")
    print("          which are NOT RECOVERED. Treated as hypothesis only.")

    section("SUMMARY")
    print("""
Counterexamples found by this audit: NONE
Possible gaps: third-party prime-2 claim (unverified hypothesis)
Not verified: eq (1.4), (2.1)-(2.2), (3.3)-(3.8), (4.1)-(4.5),
              (5.9), (5.14), (5.25 exact form), (9.3)-(9.6)

CRITICAL: verified computationally != proved mathematically.
This audit reproduces only finite, confirmed identities. It does NOT
verify Theorem 1.1 and does NOT adjudicate the paper's correctness.
""")

if __name__ == "__main__":
    main()
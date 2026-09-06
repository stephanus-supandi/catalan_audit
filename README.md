# Catalan Constant — Exact Computational Audit

Target paper: Z.-W. Sun, "Catalan's constant is irrational", arXiv:2609.04176v1.

## Scope rule
Only equations traceable to the original paper are implemented.
All MathML equations were stripped during HTML extraction and the
PDF/LaTeX source is not reachable through available parsers, so the
majority of the paper's constructions are NOT implemented.

## Confirmed equations (multi-source, traceable)
- (1.1)  T_m = sum_{r>=0} (-1)^r / (2m+2r+1)^2
- (1.2)  u_m = T_m / (2m+1)
- (1.3)  T_m + T_{m+1} = 1/(2m+1)^2

## Exact finite recurrence (derived by telescoping from (1.1))
    T_m^{(N)} + T_{m+1}^{(N)} - 1/(2m+1)^2 = (-1)^{N-1} / (2m+2N+1)^2

## Not implemented — SOURCE AMBIGUOUS
(1.4), (2.1), (2.2), (3.3)-(3.8), (4.1)-(4.5),
(5.9), (5.14), (5.25), (9.3)-(9.6)

## Critical rule
verified computationally != proved mathematically
Report status as VERIFIED FOR TESTED PARAMETERS or NOT VERIFIED.
Never report PROOF VERIFIED.

## Run
    pip install -r requirements.txt
    python experiments/run_audit.py
    pytest -q tests/
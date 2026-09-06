# Catalan Constant — Exact Computational Audit

Target paper: Z.-W. Sun, "Catalan's constant is irrational", arXiv:2609.04176v1.

## Scope rule

Only equations traceable to the original paper are implemented.

All MathML equations were stripped during HTML extraction and the
PDF/LaTeX source is not reachable through available parsers, so the
majority of the paper's constructions are **NOT implemented**.

## Confirmed equations (multi-source, traceable)

### Equation (1.1)

$$
T_m = \sum_{r=0}^{\infty}
\frac{(-1)^r}{(2m+2r+1)^2}
$$

### Equation (1.2)

$$
u_m = \frac{T_m}{2m+1}
$$

### Equation (1.3)

$$
T_m + T_{m+1}
=
\frac{1}{(2m+1)^2}
$$

## Exact finite recurrence

Derived by telescoping from (1.1).

For the truncated tail

$$
T_m^{(N)}
=
\sum_{r=0}^{N-1}
\frac{(-1)^r}{(2m+2r+1)^2},
$$

the exact finite identity is

$$
T_m^{(N)} + T_{m+1}^{(N)}
-
\frac{1}{(2m+1)^2}
=
\frac{(-1)^{N-1}}
{(2m+2N+1)^2}.
$$

This identity is checked using exact rational arithmetic.

## Not implemented — SOURCE AMBIGUOUS

The following equations could not be reconstructed reliably from
the available source material:

$$
(1.4),\quad
(2.1),\quad
(2.2),\quad
(3.3)-(3.8),\quad
(4.1)-(4.5),
$$

$$
(5.9),\quad
(5.14),\quad
(5.25),\quad
(9.3)-(9.6).
$$

These are therefore **NOT implemented**.

## Critical rule

> **verified computationally != proved mathematically**

Report status as:

- **VERIFIED FOR TESTED PARAMETERS**
- **NOT VERIFIED**

Never report **PROOF VERIFIED**.

The audit does **not** establish the correctness or incorrectness
of the paper's main theorem.

## Computational audit

The audit uses exact rational arithmetic where applicable.

The current implementation checks:

- finite tail recurrence;
- weighted-tail consistency;
- selected 2-adic integrality properties;
- automated unit tests.

The paper-specific matrix, determinant, p-adic, and final asymptotic
ledger constructions remain outside the current verification scope.

## Run

```bash
pip install -r requirements.txt
python experiments/run_audit.py
pytest -q tests/

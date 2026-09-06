"""Guards: ensure unrecovered equations are NOT silently implemented."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest

from src.matrices import ResidualMatrix
from src import determinants, bounds

def test_residual_matrix_not_implemented():
    with pytest.raises(NotImplementedError):
        ResidualMatrix(n=4, B=2)

def test_determinants_not_implemented():
    with pytest.raises(NotImplementedError):
        determinants.cauchy_paper_form()

def test_final_ledger_not_implemented():
    with pytest.raises(NotImplementedError):
        bounds.final_ledger()
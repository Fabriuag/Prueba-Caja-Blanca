
import pytest
from process import process


# PRIMERA ETAPA: COBERTURA DE SENTENCIAS
@pytest.mark.statement_coverage
@pytest.mark.parametrize(
    "values, expected",
    [
        ([4], ["positivo", "par"]),
    ],
)
def test_statement_coverage(values, expected):
    assert process(values) == expected


# SEGUNDA ETAPA: COBERTURA DE RAMAS
@pytest.mark.branch_coverage
@pytest.mark.parametrize(
    "values, expected",
    [
        ([4], ["positivo", "par"]),
        ([-3], []),
        ([], []),
    ],
)
def test_branch_coverage(values, expected):
    assert process(values) == expected


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


# TERCERA ETAPA: COBERTURA DE CAMINOS
@pytest.mark.path_coverage
@pytest.mark.parametrize(
    "values, expected",
    [
        ([4, 6], ["positivo", "par", "positivo", "par"]),  # A -> A
        ([4, 5], ["positivo", "par", "positivo"]),         # A -> B
        ([4, 0], ["positivo", "par", "par"]),              # A -> C
        ([4, -3], ["positivo", "par"]),                    # A -> D

        ([3, 6], ["positivo", "positivo", "par"]),         # B -> A
        ([3, 5], ["positivo", "positivo"]),                # B -> B
        ([3, 0], ["positivo", "par"]),                     # B -> C
        ([3, -3], ["positivo"]),                           # B -> D

        ([-2, 6], ["par", "positivo", "par"]),            # C -> A
        ([-2, 5], ["par", "positivo"]),                   # C -> B
        ([-2, 0], ["par", "par"]),                         # C -> C
        ([-2, -3], ["par"]),                               # C -> D

        ([-1, 6], ["positivo", "par"]),                    # D -> A
        ([-1, 5], ["positivo"]),                           # D -> B
        ([-1, 0], ["par"]),                                # D -> C
        ([-1, -3], []),                                    # D -> D
    ],
)
def test_path_coverage(values, expected):
    assert process(values) == expected

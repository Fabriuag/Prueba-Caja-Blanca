import pytest
from process import process


@pytest.mark.statement_coverage
@pytest.mark.parametrize(
    "values, expected",
    [
        ([4], ["positivo", "par"]),
    ],
)
def test_statement_coverage(values, expected):
    assert process(values) == expected

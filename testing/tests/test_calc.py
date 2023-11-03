import pytest

from testing.calc import addition, division, multiplication, subtraction


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (+1, 2, 3),
        (1, 2, 3),
        (0, 1, 1),
        (1, 0, 1),
        (100500, 100500, 201000),
    ],
)
def test_addition(a, b, expected):
    actual = addition(a, b)
    assert actual == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 1, 0),
        (0, 1, -1),
        (-1, -2, 1),
        (1.1, 2.1, -1.0),
    ],
)
def test_substraction(a, b, expected):
    actual = subtraction(a, b)
    assert actual == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [(10, 2, 5), (1, 1, 1), (0, 1, 0)],
)
def test_division(a, b, expected):
    actual = division(a, b)
    assert actual == expected


def test_division_to_zero():
    with pytest.raises(ValueError):
        division(1, 0)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 1, 1),
        (0, 1, 0),
        (-1, -2, 2),
    ],
    ids=[
        "Multiplication to 1",
        "Multiplication to 0",
        "Multiplication with < 0 numbers",
    ],
)
def test_multiplication(a, b, expected):
    result = multiplication(a, b)
    assert result == expected

import pytest

from sprint_4_testing.calc import calculation_by_str


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("1+1", 2),
        ("-1+1", 0),
        ("10+1", 11),
    ],
)
def test_calculation_by_str_for_addition(input_str, expected):
    result: int = calculation_by_str(input_str)
    assert result == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("1-1", 0),
        ("-1-1", -2),
        ("10-1", 9),
    ],
)
def test_calculation_by_str_for_sub(input_str, expected):
    result: int = calculation_by_str(input_str)
    assert result == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("1/1", 1),
        ("2/1", 2),
        ("2/2", 1),
    ],
)
def test_calculation_by_str_for_div(input_str, expected):
    result: int = calculation_by_str(input_str)
    assert result == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("1*1", 1),
        ("2*1", 2),
    ],
)
def test_calculation_by_str_for_multiplication(input_str, expected):
    result: int = calculation_by_str(input_str)
    assert result == expected


@pytest.mark.parametrize(
    "a,b",
    [
        ("1", "1"),
        ("2", "1"),
    ],
)
@pytest.mark.parametrize(
    "sign",
    [
        "(",
        "a",
        "=",
        "|",
        "<>",
    ],
)
def test_calculation_by_str_user_errors_sign(a, b, sign):
    input_str = f"{a}{sign}{b}"
    with pytest.raises(ValueError):
        calculation_by_str(input_str)


#
# @pytest.mark.parametrize(
#     "a",
#     [
#         ("1.1+2.1"),
#     ],
# )
# def test_calculation_by_str_user_errors_sign(a):
#     with pytest.raises(KeyError):
#         calculation_by_str(a)

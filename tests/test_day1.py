import pytest

from day1 import find_first_and_last_digit, find_first_and_last_digit_2


@pytest.mark.parametrize(
    "value, expected",
    # cSpell: disable
    [("1abc2", 12), ("pqr3stu8vwx", 38), ("a1b2c3d4e5f", 15), ("treb7uchet", 77)]
    # cSpell: enable
)
def test_find_first_and_last_digit(value: str, expected: int):
    assert find_first_and_last_digit(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    # cSpell: disable
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
        # extra tests not covered in default, thanks Reddit! :-D
        ("eighthree", 83),
        ("sevenine", 79),
    ],
    # cSpell: enable
)
def test_find_first_and_last_digit_2(value: str, expected: int):
    assert find_first_and_last_digit_2(value) == expected

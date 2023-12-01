import os
import os.path
import re


def find_first_and_last_digit(value: str) -> int:
    digits: list[str] = re.findall(r"\d", value)
    return int(digits[0] + digits[-1])


def part_1() -> None:
    # Read all the value from the file day1.txt
    with open(os.path.join(os.path.dirname(__file__), "day1.txt")) as f:
        lines: list[str] = f.readlines()
        res: int = sum(find_first_and_last_digit(line) for line in lines)
        print(f"Answer is: {res}")


digits_words: list[str] = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

# TIL about positive lookahead!
pattern: re.Pattern[str] = re.compile("(?=([1-9]|" + "|".join(digits_words) + "))")


def find_first_and_last_digit_2(value: str) -> int:
    def to_int(v: str) -> str:
        return v if v.isdigit() else str(digits_words.index(v) + 1)

    res: list[str] = pattern.findall(value)
    return int(to_int(res[0]) + to_int(res[-1]))


def part_2() -> None:
    with open(os.path.join(os.path.dirname(__file__), "day1.txt")) as f:
        lines: list[str] = f.readlines()
        res: int = sum(find_first_and_last_digit_2(line) for line in lines)
        print(f"Answer is: {res}")

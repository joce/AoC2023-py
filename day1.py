import re


def part_1() -> None:
    def find_first_and_last_digit_sum(value: str) -> int:
        digits = re.findall(r"\d", value)
        if len(digits) == 0:
            return 0
        return int(digits[0] + digits[-1])

    # cSpell: disable
    test: list[str] = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    # cSpell: enable
    test_result: int = 142
    total: int = 0
    for value in test:
        v = find_first_and_last_digit_sum(value)
        total += v
    print(total)
    if total != test_result:
        print("Test failed")
        return

    # Read all the value from the file day1.txt
    with open("day1.txt") as f:
        lines = f.readlines()
    total = 0
    for line in lines:
        v = find_first_and_last_digit_sum(line)
        total += v
    print(total)


def part_2() -> None:
    digits: list[str] = [
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
    rev_digits: list[str] = []
    for d in digits:
        rev_digits.append(d[::-1])

    pattern: re.Pattern[str] = re.compile("([1-9]|" + "|".join(digits) + ")")
    rev_pattern: re.Pattern[str] = re.compile("([1-9]|" + "|".join(rev_digits) + ")")

    def find_first_and_last_digit_sum(value: str) -> int:
        res: list[str] = pattern.findall(value)
        res_r: list[str] = rev_pattern.findall(value[::-1])

        def to_int(v: str) -> str:
            if v.isdigit():
                return v
            if v in digits:
                return str(digits.index(v) + 1)
            return ""

        return int(to_int(res[0]) + to_int(res_r[0][::-1]))

    # cSpell: disable
    test: list[str] = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
        # extra tests not covered in default, thanks Reddit! :-D
        "eighthree",
        "sevenine",
    ]
    # cSpell: enable
    test_result: int = 281 + 83 + 79
    total: int = 0

    for value in test:
        v = find_first_and_last_digit_sum(value)
        total += v
    print(total)
    if total != test_result:
        print("Test failed")
        return

    with open("day1.txt") as f:
        lines = f.readlines()
    total = 0
    cnt = 1
    for line in lines:
        v = find_first_and_last_digit_sum(line)
        if cnt == 1000:
            print()
        cnt += 1
        total += v
    print(total)


if __name__ == "__main__":
    part_2()
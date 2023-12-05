import os.path
import re


def parse_input(value: str) -> tuple[int, list[int], list[int]]:
    # Parse lines such as:
    re_int: re.Pattern[str] = re.compile(r"\d+")
    values: list[str] = value.split(": ")
    card_id: int = int(re_int.findall(values[0])[0])
    nums_str: str = values[1]
    num_lists: list[str] = nums_str.split("|")

    winning_nums: list[int] = [
        int(num.strip()) for num in re_int.findall(num_lists[0].strip())
    ]
    own_nums: list[int] = [
        int(num.strip()) for num in re_int.findall(num_lists[1].strip())
    ]

    return (card_id, winning_nums, own_nums)


def count_wins(winning_nums: list[int], own_nums: list[int]) -> int:
    wins: int = 0
    for num in own_nums:
        if num in winning_nums:
            wins += 1
    return wins


def score(wins: int) -> int:
    if wins == 0:
        return 0
    return 2 ** (wins - 1)


def compute_total(cards: list[str]) -> int:
    total: int = 0
    for card in cards:
        _, winning_nums, own_nums = parse_input(card)
        wins = count_wins(winning_nums, own_nums)
        total += score(wins)
    return total


def compute_cards_count(cards_def: list[str]) -> int:
    cards: list[tuple[int, list[int], list[int]]] = list(map(parse_input, cards_def))
    cache: list[int] = [-1] * len(cards)

    def compute_wins(idx: int, cnt: int) -> int:
        wins: int = cnt
        for i in range(idx, idx + cnt):
            curr_wins = cache[i]
            if curr_wins == -1:
                curr_wins: int = count_wins(cards[i][1], cards[i][2])
                cache[i] = curr_wins
            if curr_wins == 0:
                continue
            wins += compute_wins(i + 1, curr_wins)
        return wins

    return compute_wins(0, len(cards))


def compute_cards_count_iter(cards_def: list[str]) -> int:
    cards: list[tuple[int, list[int], list[int]]] = list(map(parse_input, cards_def))
    wins: int = 0
    stack: list[tuple[int, int]] = [(0, len(cards))]
    cache: list[int] = [-1] * len(cards)

    while stack:
        idx, cnt = stack.pop()
        for i in range(idx, idx + cnt):
            curr_wins = cache[i]
            if curr_wins == -1:
                curr_wins: int = count_wins(cards[i][1], cards[i][2])
                cache[i] = curr_wins
            if curr_wins > 0:
                stack.append((i + 1, curr_wins))
        wins += cnt

    return wins


def part_1() -> None:
    with open(os.path.join(os.path.dirname(__file__), "day4.txt")) as f:
        cards: list[str] = f.readlines()
        print(compute_total(cards))


def part_2() -> None:
    with open(os.path.join(os.path.dirname(__file__), "day4.txt")) as f:
        cards: list[str] = f.readlines()
        print(compute_cards_count_iter(cards))

import pytest

import day04


@pytest.mark.parametrize(
    "value, expected",
    [
        (
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            (1, [41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]),
        ),
        (
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            (2, [13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]),
        ),
        (
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            (3, [1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1]),
        ),
        (
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            (4, [41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83]),
        ),
        (
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            (5, [87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36]),
        ),
        (
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
            (6, [31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11]),
        ),
    ],
)
def test_parse_input(value: str, expected: tuple[int, list[int], list[int]]) -> None:
    assert day04.parse_input(value) == expected


@pytest.mark.parametrize(
    "winning, own, expected",
    [
        ([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53], 4),
        ([13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19], 2),
        ([1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1], 2),
        ([41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83], 1),
        ([87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36], 0),
        ([31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11], 0),
    ],
)
def test_count_wins(winning: list[int], own: list[int], expected: int) -> None:
    assert day04.count_wins(winning, own) == expected


@pytest.mark.parametrize(
    "value, expected",
    [(0, 0), (1, 1), (2, 2), (3, 4), (4, 8), (5, 16), (6, 32), (7, 64), (8, 128)],
)
def test_score(value: int, expected: int) -> None:
    assert day04.score(value) == expected


def test_day4() -> None:
    values: list[str] = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]
    assert day04.compute_total(values) == 13
    assert day04.compute_cards_count(values) == 30
    assert day04.compute_cards_count_iter(values) == 30

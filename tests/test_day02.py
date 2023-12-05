import pytest

import day02


def test_parse_game():
    game = day02.Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert game.game_id == 1

    assert game.largest_red_score == 4
    assert game.largest_green_score == 2
    assert game.largest_blue_score == 6

    game = day02.Game(
        "Game 92: 2 red, 4 green, 6 blue; 9 blue, 3 green, 6 red; 5 blue, 4 green; 3 blue, 2 green, 7 red; 4 red, 4 green, 11 blue"  # noqa
    )
    assert game.game_id == 92

    assert game.largest_red_score == 7
    assert game.largest_green_score == 4
    assert game.largest_blue_score == 11

    game = day02.Game(
        "Game 100: 9 blue, 18 green, 4 red; 5 green, 10 blue, 11 red; 1 green, 1 red; 16 green, 5 red, 1 blue"  # noqa
    )
    assert game.game_id == 100

    assert game.largest_red_score == 11
    assert game.largest_green_score == 18
    assert game.largest_blue_score == 10


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", (True, 1)),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", (True, 2)),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            (False, 3),
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            (False, 4),
        ),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", (True, 5)),
    ],
)
def test_part_1(
    value: str,
    expected: tuple[bool, int],
):
    game = day02.Game(value)
    assert game.is_game_possible(12, 13, 14) == expected[0]
    assert game.game_id == expected[1]


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 48),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 12),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            1560,
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            630,
        ),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 36),
    ],
)
def test_part_2(
    value: str,
    expected: int,
):
    game = day02.Game(value)
    assert game.smallest_power == expected

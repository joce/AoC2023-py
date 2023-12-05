import os.path
import re


class Inning:
    def __init__(self, value: str) -> None:
        red = re.findall(r"(\d+) red", value)
        green = re.findall(r"(\d+) green", value)
        blue = re.findall(r"(\d+) blue", value)

        self.red_score: int = int(red[0]) if len(red) > 0 else 0
        self.green_score: int = int(green[0]) if len(green) > 0 else 0
        self.blue_score: int = int(blue[0]) if len(blue) > 0 else 0


class Game:
    @property
    def largest_red_score(self) -> int:
        return max(inning.red_score for inning in self.innings)

    @property
    def largest_green_score(self) -> int:
        return max(inning.green_score for inning in self.innings)

    @property
    def largest_blue_score(self) -> int:
        return max(inning.blue_score for inning in self.innings)

    @property
    def smallest_power(self) -> int:
        return (
            self.largest_red_score * self.largest_green_score * self.largest_blue_score
        )

    # A game looks like this:
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    def __init__(self, value: str) -> None:
        self.game_id = int(re.findall(r"Game (\d+):", value)[0])
        value = value[value.find(":") + 1 :].strip()
        inning: str = ""
        self.innings: list[Inning] = []
        for inning in value.split(";"):
            self.innings.append(Inning(inning))

    def is_game_possible(self, red: int, green: int, blue: int) -> bool:
        return (
            self.largest_red_score <= red
            and self.largest_green_score <= green
            and self.largest_blue_score <= blue
        )


def part_1() -> None:
    with open(os.path.join(os.path.dirname(__file__), "day2.txt")) as f:
        score = 0
        lines: list[str] = f.readlines()
        line: str
        for line in lines:
            game = Game(line)
            if game.is_game_possible(12, 13, 14):
                score += game.game_id
        print(f"Answer is: {score}")


def part_2() -> None:
    with open(os.path.join(os.path.dirname(__file__), "day2.txt")) as f:
        score = 0
        lines: list[str] = f.readlines()
        line: str
        for line in lines:
            game = Game(line)
            score += game.smallest_power
        print(f"Answer is: {score}")

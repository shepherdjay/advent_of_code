import re
import math

GAME_REGEX = re.compile(r'(?P<value>\d+)\s(?P<color>\w+)')


def process_game_data(game: str) -> dict:
    game_id, game = game.split(':')

    color_values = {
        'red': 0,
        'blue': 0,
        'green': 0,
    }

    for pull in game.split(';'):
        for color_data in pull.split(','):
            group_dict = GAME_REGEX.search(color_data).groupdict()
            color, value = group_dict['color'], int(group_dict['value'])
            color_values[color] = max(color_values[color], value)
    return color_values


def check_hypothesis(color_values: dict, hypothesis: dict):
    for color, max in color_values.items():
        if hypothesis[color] < max:
            return False
    return True


def sum_of_possible(allgames: list[str], hypothesis: dict) -> int:
    processed_games = [process_game_data(game) for game in allgames]
    summed_index = 0
    for count, game in enumerate(processed_games, 1):
        if check_hypothesis(game, hypothesis):
            summed_index += count
    return summed_index


def sum_powers(allgames: list[str]) -> int:
    processed_games = [process_game_data(game) for game in allgames]
    summed_index = 0
    for game in processed_games:
        summed_index += math.prod(game.values())
    return summed_index


if __name__ == '__main__':  # pragma: no cover
    with open('advent_2023_02_input.txt', 'r') as infile:
        games = infile.readlines()
    print(sum_of_possible(games, hypothesis={'red': 12, 'green': 13, 'blue': 14}))
    print(sum_powers(games))

from typing import Tuple


def count_card(winning_numbers: set, player_numbers: set) -> Tuple[int, int]:
    """
    Returns winnings, first match is worth 1 point for each subsequent its 2x
    >>> count_card({41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53})
    (8, 4)
    >>> count_card({41, 92, 73, 84, 69}, {59, 84, 76, 51, 58, 5, 54, 83})
    (1, 1)
    """
    matches = len(winning_numbers.intersection(player_numbers))
    return 2**matches // 2, matches


def process_cards(card_list: list[str]) -> int:
    """
    >>> cards_example = [\
        'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53', \
        'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19', \
        'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1', \
        'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83', \
        'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36', \
        'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']
    >>> process_cards(cards_example)
    13
    """
    total = 0
    for idx, line in enumerate(card_list):
        card, details = line.split(':')
        winning, player = details.split('|')
        winning = set(winning.split())
        player = set(player.split())
        card_value, matches = count_card(winning, player)
        total += card_value
    return total


def process_cards_v2(card_list: list[str]) -> int:
    card_dict = {}
    for idx, card in enumerate(card_list):
        _, details = card.split(':')
        winning, player = details.split('|')
        winning = set(winning.split())
        player = set(player.split())
        card_dict[idx] = {'winning': winning, 'player': player, 'copies': 1}

    total_cards = len(card_dict)
    for card_number, card in card_dict.items():
        for _ in range(card['copies']):
            card_value, matches = count_card(card['winning'], card['player'])
            total_cards += matches
            shift = 1
            for _ in range(matches):
                card_dict[card_number + shift]['copies'] += 1
                shift += 1

    return total_cards


if __name__ == '__main__':  # pragma: no cover
    with open('advent_2023_04_input.txt', 'r') as infile:
        card_string = infile.read().splitlines()
    print(process_cards(card_string))
    print(process_cards_v2(card_string))

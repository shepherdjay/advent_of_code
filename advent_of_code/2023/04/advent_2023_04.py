from typing import Tuple

def count_card(winning_numbers: set, player_numbers: set) -> Tuple[int,int]:
    """
    Returns winnings, first match is worth 1 point for each subsequent its 2x
    >>> count_card({41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53})
    8
    >>> count_card({41, 92, 73, 84, 69}, {59, 84, 76, 51, 58,  5, 54, 83})
    1
    """
    matches = len(winning_numbers.intersection(player_numbers))
    return 2**matches // 2, matches

def update_for_matches(idx, matches, my_list):
    """
    updates a list in place with copy of elements
    """
    right_idx = idx + matches
    for _ in range(matches):
        my_list.insert(right_idx, my_list[right_idx])
        right_idx -= 1


def process_cards(card_list: list[str], part2=False) -> Tuple[int, int]|int:
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
    >>> process_cards(cards_example, part2=True)
    (13, 30)
    """
    total = 0
    for idx, line in enumerate(card_list):
        card, details = line.split(':')
        winning, player = details.split('|')
        winning = set(winning.split())
        player = set(player.split())
        card_value, matches = count_card(winning, player)
        total += card_value
        if part2:
            update_for_matches(idx, matches, card_list)
    if part2:
        return total, len(card_list)
    return total

if __name__ == '__main__': # pragma: no cover
    with open("advent_2023_04_input.txt", "r") as infile:
        card_string = infile.read().splitlines()
    print(process_cards(card_string))
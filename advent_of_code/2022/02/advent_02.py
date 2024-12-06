if __name__ == "__main__":
    with open("advent_02_input.txt", "r") as infile:
        cheat_sheet = []
        for line in infile:
            x, y = line.split()
            cheat_sheet.append((x, y))

    KEY = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors",
    }

    UPDATED_KEY = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
        "X": "LOSE",
        "Y": "TIE",
        "Z": "WIN",
        "Rock": "X",
        "Paper": "Y",
        "Scissors": "Z",
    }

    SCORES = {"Rock": 1, "Paper": 2, "Scissors": 3, "WIN": 6, "TIE": 3, "LOSE": 0}

    WIN_MAP = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

    def decide_winner(opponent, response):
        if WIN_MAP[opponent] == response:
            return "LOSE"
        elif WIN_MAP[response] == opponent:
            return "WIN"
        else:
            return "TIE"

    def calculate_round(opponent_key, response_key):
        """
        >>> calculate_round("A", "Y")
        8
        >>> calculate_round("B", "X")
        1
        >>> calculate_round("C", "Z")
        6
        """
        opponent = KEY[opponent_key]
        response = KEY[response_key]
        selection_value = SCORES[response]
        result_value = SCORES[decide_winner(opponent, response)]
        return selection_value + result_value

    print(sum([calculate_round(x, y) for x, y in cheat_sheet]))

    def find_the_right_response(opponent_key, response_key):
        opponent = UPDATED_KEY[opponent_key]
        result_needed = UPDATED_KEY[response_key]
        for shape in WIN_MAP.keys():
            if decide_winner(opponent, shape) == result_needed:
                return UPDATED_KEY[shape]

    new_scores = []
    for opponent_key, response_key in cheat_sheet:
        right_response_key = find_the_right_response(opponent_key, response_key)
        new_scores.append(calculate_round(opponent_key, right_response_key))

    print(sum(new_scores))

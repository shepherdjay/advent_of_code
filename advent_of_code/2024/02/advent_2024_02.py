def check_level_safety(level: list, dampen=False) -> bool:
    """
    Given a level return a bool of True if safe
    """
    increasing = None
    prev_value = level[0]

    if level[1] > prev_value:
        increasing = True
    elif level[1] < prev_value:
        increasing = False
    else:
        return False

    for value in level[1::]:
        # early exit
        if prev_value == value:
            return False
        if increasing and value < prev_value:
            return False
        if not increasing and value > prev_value:
            return False
        if abs(prev_value - value) > 3:
            return False

        prev_value = value

    return True


def safe_level_count(report: list[list[int]]) -> int:
    return sum([check_level_safety(level) for level in report])


if __name__ == "__main__":  # pragma: no cover
    with open("advent_2024_02_input.txt", 'r') as infile:
        reports = []
        for line in infile:
            reports.append([int(x) for x in line.split()])
    print(safe_level_count(reports))
def analyze_row(row, increasing, max_diff=3):
    prev_value = row[0]

    for index, value in enumerate(row):
        if index == 0:
            continue

        if prev_value == value:
            return False
        elif increasing and value < prev_value:
            return False
        elif not increasing and value > prev_value:
            return False
        elif abs(prev_value - value) > max_diff:
            return False

        prev_value = value

    return True


def check_level_safety(level: list, dampen=False) -> bool:
    """
    Given a level return a bool of True if safe
    """

    if level[0] > level[1]:
        increasing = False
    elif level[0] < level[1]:
        increasing = True
    else:
        return False

    if not dampen:
        return analyze_row(level, increasing=increasing)
    else:
        available_lists = []
        for i in range(len(level)):
            available_lists.append(level[:i] + level[i + 1 :])

        results = [check_level_safety(row) for row in available_lists]

        return any(results)


def safe_level_count(report: list[list[int]], dampen=False) -> int:
    return sum([check_level_safety(level, dampen) for level in report])


if __name__ == "__main__":  # pragma: no cover
    with open("advent_2024_02_input.txt", "r") as infile:
        reports = []
        for line in infile:
            reports.append([int(x) for x in line.split()])
    print(safe_level_count(reports))
    print(safe_level_count(reports, dampen=True))

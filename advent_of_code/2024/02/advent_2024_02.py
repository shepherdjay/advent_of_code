def analyze_row(row: list, increasing: bool, max_diff: int = 3) -> bool:
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


def generate_subrows(row: list) -> list[list]:
    subrows = []
    for i in range(len(row)):
        new_row = row[:]
        new_row.pop(i)
        subrows.append(new_row)
    return subrows


def check_level_safety(level: list, dampen=False) -> bool:
    """
    Given a level return a bool of True if safe
    If dampen True recurse sublevels
    """
    if not dampen:
        if level[0] > level[1]:
            increasing = False
        elif level[0] < level[1]:
            increasing = True
        else:
            return False

        return analyze_row(level, increasing=increasing)
    else:
        results = [check_level_safety(row, dampen=False) for row in generate_subrows(level)]
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

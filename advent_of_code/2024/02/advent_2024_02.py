def check_level_safety(level: list, dampen=False) -> bool:
    """
    Given a level return a bool of True if safe
    """
    prev_value = level[0]
    increasing = None
    fault = False

    if level[1] > prev_value:
        increasing = True
    elif level[1] < prev_value:
        increasing = False
    else:
        fault = True

    for index, value in enumerate(level[1::]):
        # early exit
        if prev_value == value:
            fault = True
        elif increasing and value < prev_value:
            fault = True
        elif not increasing and value > prev_value:
            fault = True
        elif abs(prev_value - value) > 3:
            fault = True
        else:
            pass

        if fault and dampen:
            recheck_list = level[:index] + level[index + 1 : :]
            if check_level_safety(recheck_list, dampen=False) is False:
                return False

        if fault and not dampen:
            return False

        fault = False
        prev_value = value

    return True


def safe_level_count(report: list[list[int]], dampen=False) -> int:
    return sum([check_level_safety(level, dampen) for level in report])


if __name__ == "__main__":  # pragma: no cover
    with open("advent_2024_02_input.txt", "r") as infile:
        reports = []
        for line in infile:
            reports.append([int(x) for x in line.split()])
    print(safe_level_count(reports))
    print(safe_level_count(reports, dampen=True))

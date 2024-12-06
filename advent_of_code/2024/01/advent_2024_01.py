def get_lists(input_file) -> tuple[list, list]:
    list_a = []
    list_b = []
    with open(input_file, 'r') as infile:
        for line in infile:
            a, b = line.split()
            list_a.append(int(a))
            list_b.append(int(b))

    return (list_a, list_b)


def find_total_distance(list_a, list_b):
    list_a.sort()
    list_b.sort()
    paired_list = [pair for pair in zip(list_a, list_b)]
    running_total = 0
    for x, y in paired_list:
        running_total += abs(y - x)
    return running_total


def single_similarity(n, list_b):
    count = 0
    for number in list_b:
        if n == number:
            count += 1
    return count * n


def calculate_similarity(list_a, list_b):
    total = 0
    for n in list_a:
        total += single_similarity(n, list_b)
    return total


if __name__ == '__main__':  # pragma: no cover
    list_a, list_b = get_lists('advent_2024_01_input.txt')
    print(find_total_distance(list_a, list_b))
    print(calculate_similarity(list_a, list_b))

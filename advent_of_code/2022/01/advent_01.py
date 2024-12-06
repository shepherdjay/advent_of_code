if __name__ == '__main__':
    with open('advent_01_input.txt', 'r') as infile:
        raw_lines = infile.readlines()

    all_sets = []

    while True:
        index = 0
        for entry in raw_lines:
            if entry.strip() == '':
                break
            else:
                index += 1
        else:
            an_elf_inventory = [int(x.strip()) for x in raw_lines]
            all_sets.append(an_elf_inventory)
            break
        an_elf_inventory = [int(x.strip()) for x in raw_lines[0:index]]
        all_sets.append(an_elf_inventory)
        raw_lines = raw_lines[index + 1 : :]

    sums = []

    for set in all_sets:
        sums.append(sum(set))

    # Part 1
    print(max(sums))

    # Part 2
    sums.sort(reverse=True)
    print(sum(sums[0:3]))

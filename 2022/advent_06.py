from collections import deque


def find_marker(datastream: str) -> int:
    """
    >>> find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz')
    5
    >>> find_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
    10
    """
    queue = deque(maxlen=4)

    marker = 0
    for char in datastream:
        marker += 1
        queue.append(char)
        if len(set(queue)) == 4:
            break

    return marker


if __name__ == '__main__':
    with open('advent_06_input.txt', 'r') as infile:
        datastream = infile.read().strip()

    print(find_marker(datastream))

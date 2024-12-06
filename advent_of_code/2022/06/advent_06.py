from collections import deque


def find_marker(datastream: str, marker_distinction: int = 4) -> int:
    """
    >>> find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz")
    5
    >>> find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
    10
    """
    queue = deque(maxlen=marker_distinction)

    marker = 0
    for char in datastream:
        marker += 1
        queue.append(char)
        if len(set(queue)) == marker_distinction:
            break

    return marker


if __name__ == "__main__":
    with open("advent_06_input.txt", "r") as infile:
        datastream = infile.read().strip()

    print(find_marker(datastream, marker_distinction=4))
    print(find_marker(datastream, marker_distinction=14))

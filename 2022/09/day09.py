import math


class Point:
    def __init__(self, x, y, head: "Point" = None):
        self.x = x
        self.y = y
        self.head = head

        self.visited = [(self.x, self.y)]

    def reduce_distance(self):
        x1, y1 = self.head.x, self.head.y
        x2, y2 = self.x, self.y

        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        if (
            distance == 0
        ):  # They are already in the same place so no need to calculate a vector
            unit_vector = (0, 0)
        else:
            unit_vector = ((x2 - x1) / distance, (y2 - y1) / distance)

        self.x = round(x1 + unit_vector[0])
        self.y = round(y1 + unit_vector[1])


def follow_the_leader(instructions, head, tails):
    # updates head then updates all tails, returning the length of visited points for the last tail

    for direction, steps in instructions:
        steps = int(steps)
        for _ in range(steps):
            if direction == "R":
                head.x += 1
            elif direction == "L":
                head.x -= 1
            elif direction == "U":
                head.y += 1
            elif direction == "D":
                head.y -= 1

            for tail in tails:
                tail.reduce_distance()
                tail.visited.append((tail.x, tail.y))

    last_tail = tails[-1]
    unique_visits = set(last_tail.visited)

    return len(unique_visits)


def play_follow_the_leader(num_of_tails: int = 1):
    head = Point(1000, 1000)
    tails = []
    cur_head = head

    for _ in range(num_of_tails):
        new_tail = Point(1000, 1000, cur_head)
        tails.append(new_tail)
        cur_head = new_tail

    return follow_the_leader(instructions, head=head, tails=tails)


if __name__ == "__main__":
    with open("day09_input.txt", "r") as elf_file:
        instructions = [line.strip().split() for line in elf_file]

    # PART 1
    print(play_follow_the_leader())

    # PART 2
    print(play_follow_the_leader(num_of_tails=9))

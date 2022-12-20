import copy
import heapq
import re
from collections import namedtuple, deque

Valve = namedtuple('Valve', 'id,flow,neighbors')


class ValveTree(list):
    """ This exists to support easy index reference by string """

    def __init__(self, valves: list):
        self.valves = valves
        self._spt = None
        super().__init__(valves)

    @property
    def spt(self):
        if self._spt is None:
            self.generate_spt()
        return self._spt

    def generate_spt(self):
        shortest_tree = {}
        for valve in self.valves:
            starting = valve
            node_map = {node: (float('inf'), []) for node in self.valves}
            node_map[starting] = (0, [starting])
            min_dist = [(0, starting)]
            visited = set()

            while min_dist:
                cur_dist, cur = heapq.heappop(min_dist)
                if cur in visited:
                    continue
                visited.add(cur)

                for neighbor_id in cur.neighbors:
                    neighbor = self.__getitem__(neighbor_id)
                    if neighbor in visited:
                        continue
                    this_dist = cur_dist + 1
                    if this_dist < node_map[neighbor][0]:
                        node_map[neighbor] = (this_dist, node_map[cur][1] + [neighbor])
                        heapq.heappush(min_dist, (this_dist, neighbor))
            shortest_tree[valve] = node_map
        self._spt = shortest_tree
        return shortest_tree

    def __getitem__(self, item: str | int):
        if isinstance(item, int):
            return super().__getitem__(item)
        for valve in self.valves:
            if valve.id == item:
                return valve

    def get_relief_nodes(self):
        return [node for node in self if node.flow > 0]

    def construct_relief_node_tree(self, start_node):
        """
        Using the full valve tree and the spt algorithm construct a dictionary whose keys are the start node and all relief
        nodes. The value is a tuple of all other nodes and their cost from that node
        """
        interesting_nodes = self.get_relief_nodes()
        interesting_nodes.insert(0, start_node)

        new_tree = {}
        for node_a in interesting_nodes:
            new_tree[node_a] = {}
            for node_z in interesting_nodes:
                if node_a == node_z:
                    continue
                new_tree[node_a][node_z] = self.cost_between_nodes(node_a.id, node_z.id) + 1
        return new_tree

    def cost_between_nodes(self, a_node_id: str, z_node_id: str):
        a_node = self[a_node_id]
        z_node = self[z_node_id]
        return self.spt[a_node][z_node][0]

    def depth_limited_search(self, starting_node, cost_limit):
        relief_matrix = self.construct_relief_node_tree(starting_node)
        stack = deque()
        stack.append((starting_node, cost_limit, 0, set()))
        max_relief = None

        while stack:
            node, cost_limit, relief, visited = stack.pop()

            if cost_limit < 0:
                continue
            if not max_relief or relief > max_relief:
                max_relief = relief
            if node not in visited:
                for neighbor, cost in relief_matrix[node].items():
                    neighbor_set = copy.deepcopy(visited)
                    neighbor_set.add(node)
                    neighbor_relief = relief + (node.flow * cost_limit)
                    neighbor_limit = cost_limit - cost
                    if neighbor_relief < max_relief:
                        continue
                    stack.appendleft((neighbor, neighbor_limit, neighbor_relief, neighbor_set))
        return max_relief

def relieve_pressure(tree: ValveTree, timer: int, starting_node_id: str = 'A'):
    starting_node = tree[starting_node_id]
    return tree.depth_limited_search(starting_node, cost_limit=timer)


def parse_line(line: str):
    valve_regex = re.compile(r'Valve (.+) has flow rate=(\d+); tunnels? leads? to valves? (.+)')
    valve_id, flow_rate, neighbors_raw = valve_regex.search(line).groups()
    neighbors = tuple(neighbors_raw.split(', '))
    return Valve(id=valve_id, flow=int(flow_rate), neighbors=neighbors)


if __name__ == '__main__':
    with open('day16_input.txt', 'r') as elf_file:
        valves = [parse_line(line.strip()) for line in elf_file]

    tree = ValveTree(valves)

    print(tree.depth_limited_search(starting_node=tree['AA'], cost_limit=30))

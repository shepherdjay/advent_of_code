import copy
import heapq
import re
from collections import namedtuple
import itertools
import tqdm
import functools

Valve = namedtuple('Valve', 'id,flow,neighbors')


class ValveTree:
    """ This exists to support easy index reference by string """

    def __init__(self, valves: list):
        self.valves = frozenset(valves)
        self._dfs_cache = {}

    def __hash__(self):
        return hash(self.valves)

    @functools.cached_property
    def spt(self):
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
        return shortest_tree

    def __getitem__(self, item: str | int):
        if isinstance(item, int):
            raise TypeError
        for valve in self.valves:
            if valve.id == item:
                return valve

    @functools.lru_cache
    def get_relief_nodes(self):
        return [valve for valve in self.valves if valve.flow > 0]

    @functools.lru_cache
    def construct_relief_node_tree(self, start_node):
        """
        Using the full valve tree and the spt algorithm construct a dictionary whose keys are the start node and all relief
        nodes. The value is a tuple of all other nodes and their cost from that node
        """
        interesting_nodes = self.get_relief_nodes()
        interesting_nodes.insert(0, start_node)

        new_tree = {}
        for node_a in interesting_nodes:
            new_tree[node_a] = []
            for node_z in interesting_nodes:
                if node_a == node_z:
                    continue
                new_tree[node_a].append((node_z, self.cost_between_nodes(node_a.id, node_z.id) + 1))
        return new_tree

    @functools.lru_cache
    def cost_between_nodes(self, a_node_id: str, z_node_id: str):
        a_node = self[a_node_id]
        z_node = self[z_node_id]
        return self.spt[a_node][z_node][0]

    def dfs(self, tree, node, time, relief=None, visited=None):

        if visited is None:
            visited = set()
        else:
            visited = visited
        if relief is None:
            relief = 0

        max_relief = relief
        cache_key = (node, time, relief)
        if cache_key in self._dfs_cache:
            return self._dfs_cache[cache_key]

        visited.add(node)
        for neighbor, cost in tree[node]:
            if neighbor in visited:
                continue
            rem_time = time - cost
            if rem_time <= 0:
                continue

            neighbor_relief = relief + (neighbor.flow * rem_time)
            neighbor_set = copy.deepcopy(visited)
            max_relief = max(max_relief, self.dfs(tree, neighbor, rem_time, neighbor_relief, neighbor_set))
        self._dfs_cache[cache_key] = max_relief
        return max_relief

    def dfs_part2(self, starting_node, cost_limit):
        relief_matrix = self.construct_relief_node_tree(starting_node)
        max_relief = 0

        all_nodes_minus_a = set([k for k in relief_matrix.keys() if k is not starting_node])
        visiting_sets = list(self.powerset(all_nodes_minus_a))
        for visit_set in tqdm.tqdm(visiting_sets):
            my_no_visit = set(visit_set)

            eleph_no_visit = set()
            for key in relief_matrix.keys():
                if key not in my_no_visit:
                    eleph_no_visit.add(key)

            my_relief = self.dfs(tree=relief_matrix, node=starting_node, visited=my_no_visit, time=cost_limit)
            eleph_relief = self.dfs(tree=relief_matrix, node=starting_node, visited=eleph_no_visit, time=cost_limit)
            max_relief = max(max_relief, my_relief + eleph_relief)

        return max_relief

    @staticmethod
    def powerset(iterable):
        s = list(iterable)
        return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(1, len(s) + 1))


def parse_line(line: str):
    valve_regex = re.compile(r'Valve (.+) has flow rate=(\d+); tunnels? leads? to valves? (.+)')
    valve_id, flow_rate, neighbors_raw = valve_regex.search(line).groups()
    neighbors = tuple(neighbors_raw.split(', '))
    return Valve(id=valve_id, flow=int(flow_rate), neighbors=neighbors)


if __name__ == '__main__':
    with open('day16_input.txt', 'r') as elf_file:
        valves = [parse_line(line.strip()) for line in elf_file]

    tree = ValveTree(valves)
    starting_node = tree['AA']
    relief_tree = tree.construct_relief_node_tree(starting_node)

    print(tree.dfs(tree=relief_tree, node=starting_node, time=30))
    print(len(tree._dfs_cache))

    # print(tree.dfs_part2(starting_node=tree['AA'], cost_limit=26))

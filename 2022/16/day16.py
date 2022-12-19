from dataclasses import dataclass, field
import heapq
import itertools
import re


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


@dataclass(order=True)
class Valve:
    id: str = field()
    flow: int = field()
    neighbors: set[str] | None = field(default_factory=set)

    def __hash__(self):
        return hash(self.__repr__())

class Erupt(Exception):
    pass

class Volcano:
    def __init__(self, timer):
        self.timer = timer
        self.relief = 0
        self.open_valves = list()

    def _tick(self):
        self.relief += sum((valve.flow for valve in self.open_valves))
        self.timer -= 1
        if self.timer == 0:
            raise Erupt

    def move(self, i):
        for _ in range(i):
            self._tick()

    def open_valve(self, valve: Valve):
        self._tick()
        self.open_valves.append(valve)



def get_relief_nodes(tree):
    return [node for node in tree if node.flow > 0]

def simulate_path(path, relief_nodes, timer):
    volcano = Volcano(timer=timer)
    try:
        for valve in path:
            volcano.move()
            if valve in relief_nodes:
                volcano.open_valve(valve)
        for i in range(timer - volcano.timer):
            volcano.move()
    except Erupt:
        return volcano.relief, path

def relieve_pressure(valve_tree, timer: int, starting_node_id: str='A'):
    relief_nodes = get_relief_nodes(valve_tree)
    paths = generate_possible_paths(starting_node_id=starting_node_id, valve_tree=valve_tree)

    relief_paths = [simulate_path(path, relief_nodes=relief_nodes, timer=timer) for path in paths]


    relief_paths.sort(reverse=True)
    best_path = relief_paths[0]
    return best_path[0], [valve.id for valve in best_path[1]]

def cost_between_nodes(a_node_id: str, z_node_id: str, tree: ValveTree):
    a_node = tree[a_node_id]
    z_node = tree[z_node_id]
    return tree.spt[a_node][z_node][0]

def generate_possible_paths(starting_node_id, valve_tree: ValveTree):
    relief_nodes = get_relief_nodes(valve_tree)
    relief_node_ordering = map(list, itertools.permutations(relief_nodes))

    paths = []
    for path in relief_node_ordering:
        path.insert(0, valve_tree[starting_node_id])
        full_path = []
        for index, valve in enumerate(path):
            try:
                next_valve = path[index + 1]
                node_path = valve_tree.spt[valve][next_valve][1][1:]
                full_path.extend(node_path)
            except IndexError:
                continue
        paths.append(full_path)

    return paths

def parse_line(line:str):
    valve_regex = re.compile(r'Valve (.+) has flow rate=(\d+); tunnels? leads? to valves? (.+)')
    valve_id, flow_rate, neighbors_raw = valve_regex.search(line).groups()
    neighbors = neighbors_raw.split(', ')
    return Valve(id=valve_id, flow=int(flow_rate), neighbors=set(neighbors))
from dataclasses import dataclass, field


class ValveTree(list):
    """ This exists to support easy index reference by string """

    def __init__(self, valves: list):
        self.valves = valves
        super().__init__(valves)

    def __getitem__(self, item: str | int):
        if isinstance(item, int):
            return super().__getitem__(item)
        for valve in self.valves:
            if valve.id == item:
                return valve


@dataclass
class Valve:
    id: str = field(compare=True)
    flow: int
    neighbors: set[str] | None = field(default_factory=set)


def relieve_pressure(valve_tree, timer):
    pass


def find_common_ancester(valves, valve_tree):
    pass

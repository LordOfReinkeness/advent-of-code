import numpy as np

from challenges._2025._8.input_parse import parse_input

class JunctionBox:

    circuit_size = 0

    def __init__(self, position):
        self.position = position
        self.neighbours = []
        self.visited = False

    def connect(self, other: JunctionBox):
        self.neighbours.append(other)
        other.neighbours.append(self)

        if self._get_circuit_size() == JunctionBox.circuit_size:
            return True

        self.reset_visits()
        return False

    def _get_circuit_size(self):

        if self.visited:
            return -1
        else:
            self.visited = True

        graph = 1
        for neighbour in self.neighbours:
            if not neighbour.visited:
                graph += neighbour._get_circuit_size()

        return graph

    def reset_visits(self):
        self.visited = False

        for neighbour in self.neighbours:
            if neighbour.visited:
                neighbour.reset_visits()


def main(data):
    data = parse_input(data)
    # Your challenges for AOC 2025 day 8 part 2 goes here
    connections_map = {}
    JunctionBox.circuit_size = len(data)

    for idy, y_elem in enumerate(data):
        for idx, x_elem in enumerate(data):
            if idy < idx:
                connections_map[np.linalg.norm(y_elem - x_elem)] = [idy, idx]

    connections_index = [item for item in connections_map]
    connections_index.sort()

    junction_nodes = [JunctionBox(position) for position in data]

    for i in range(len(connections_index)):

        node_1: JunctionBox = junction_nodes[connections_map[connections_index[i]][0]]
        node_2: JunctionBox = junction_nodes[connections_map[connections_index[i]][1]]

        completed = node_1.connect(node_2)

        if completed:
            return node_1.position[0] * node_2.position[0]

    return 'AOC 2025 day 8 part 2'

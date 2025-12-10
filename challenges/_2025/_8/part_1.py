import numpy as np

from challenges._2025._8.input_parse import parse_input

class JunctionBox:

    def __init__(self, position):
        self.position = position
        self.neighbours = []
        self.visited = False

    def get_circuit_size(self):

        if self.visited:
            return -1
        else:
            self.visited = True

        graph = 1
        for neighbour in self.neighbours:
            if not neighbour.visited:
                graph += neighbour.get_circuit_size()

        return graph


def main(data):
    data = parse_input(data)
    # Your challenges for AOC 2025 day 8 part 1 goes here

    connections_map = {}

    for idy, y_elem in enumerate(data):
        for idx, x_elem in enumerate(data):
            if idy < idx:
                connections_map[np.linalg.norm(y_elem - x_elem)] = [idy, idx]

    connections_index = [item for item in connections_map]
    connections_index.sort()

    junction_nodes = [JunctionBox(position) for position in data]

    for i in range(1000):
        (
            junction_nodes[connections_map[connections_index[i]][0]]
             .neighbours.append(
                junction_nodes[connections_map[connections_index[i]][1]]
            )
        )

        (
            junction_nodes[connections_map[connections_index[i]][1]]
            .neighbours.append(
                junction_nodes[connections_map[connections_index[i]][0]]
            )
        )

    circuit_sizes = [junction_node.get_circuit_size() for junction_node in junction_nodes]
    circuit_sizes.sort(reverse=True)

    out = 1
    for elem in circuit_sizes[:3]:
        out *= elem

    return out
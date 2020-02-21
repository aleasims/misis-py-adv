from node import Node


class Graph:
    def __init__(self):
        pass

    @classmethod
    def from_adjacency_map(self, adj: dict):
        raise NotImplementedError

    def in_graph(self, node: Node) -> bool:
        raise NotImplementedError

    def add_node(self, node: Node, links: list):
        raise NotImplementedError


class WeightedGraph(Graph):
    pass

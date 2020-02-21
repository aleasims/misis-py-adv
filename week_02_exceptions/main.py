from graph import Graph
from node import Node


if __name__ == "__main__":
    n1, n2, n3 =  Node(), Node(), Node()
    adj = {
        n1: [n2, n3],
        n2: [n3, n1],
        n3: [n2, n1]
    }

    g = Graph.from_adjacency_map(adj)

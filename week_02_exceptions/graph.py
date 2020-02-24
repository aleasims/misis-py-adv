from node import Node


class Graph:
    def __init__(self, adj: dict):
        self.adj = adj

    @classmethod
    def from_dict(cls, input_dict: dict):
        d = input_dict.copy()
        for node, links in input_dict.items():
            for link in links:
                if link not in d:
                    d[link] = [node]
                else:
                    if node not in d[link]:
                        d[link].append(node)
        return cls(d)
    
    def __str__(self):
        return '<Graph {}>'.format(self.adj)

    def in_graph(self, node: Node) -> bool:
        raise NotImplementedError

    def add_node(self, node: Node):
        raise NotImplementedError
    
    def add_edge(self, node1: Node, node2: Node):
        raise NotImplementedError


class WeightedGraph(Graph):
    pass


if __name__ == "__main__":
    n1, n2, n3 = Node(), Node(), Node()
    d = {
        n1: [n2],
        n2: [n3]
    }
    print(d)
    g = Graph.from_dict(d)
    print(g)

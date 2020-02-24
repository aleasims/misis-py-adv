class Node:
    _next_id = 0
    def __init__(self, label='') -> None:
        self.id = Node._next_id
        Node._next_id += 1

    def __repr__(self) -> str:
        return '<Node_{}>'.format(self.id)

    def __hash__(self) -> int:
        return self.id


if __name__ == "__main__":
    n1 = Node()
    n2 = Node()
    assert n1.id != n2.id
    n3 = Node()
    d = {n1: [n2, n3]}
    print(d)

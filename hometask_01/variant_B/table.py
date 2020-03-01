# class TableError


class Table:
    def __init__(self, columns: list):
        # self.rows = ?
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    @property
    def next_index(self) -> int:
        raise NotImplementedError

    def validate(self, row):
        raise NotImplementedError

    def add_row(self, row: list) -> int:
        raise NotImplementedError

    def get_row(self, index: int) -> list:
        raise NotImplementedError

    def remove_row(self, index: int):
        raise NotImplementedError


def test():
    cols = ['A', 'B', 'C']
    t = Table(cols)
    t.add_row([1, 2, 3])
    assert repr(t) == 'A B C\n1 2 3'
    assert str(t) == "<Table with ['A', 'B', 'C']>"
    r = t.get_row(0)
    assert r == [1, 2, 3]

    t.add_row([4, 5, 6])
    assert list(t) == [{'A': 1, 'B': 2, 'C': 3}, {'A': 4, 'B': 5, 'C': 6}]
    assert len(t) == 2


if __name__ == "__main__":
    test()

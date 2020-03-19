class TableError(Exception):
    pass


class Table:

    __slots__ = ['columns', 'rows']

    def __init__(self, columns: list):
        self.columns = columns
        self.rows = []

    def __str__(self):
        return '<Table with {}>'.format(self.columns)

    def __repr__(self):
        tmp = [' '.join(str(c) for c in self.columns)]
        for row in self.rows:
            tmp.append(' '.join(str(v) for v in row))
        return '\n'.join(tmp)

    def __len__(self):
        return len(self.rows)

    def __iter__(self):
        for row in self.rows:
            yield {name: value for name, value in zip(self.columns, row)}

    @property
    def next_index(self):
        return len(self.rows)

    def validate(self, row):
        if len(row) != len(self.columns):
            raise TableError('Incompatible row length')
        return row

    def add_row(self, row: list) -> int:
        row = self.validate(row)
        index = self.next_index
        self.rows.append(row)
        return index

    def get_row(self, index: int) -> list:
        try:
            return self.rows[index]
        except IndexError:
            return None

    def remove_row(self, index: int):
        try:
            self.rows.pop(index)
        except IndexError:
            pass


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

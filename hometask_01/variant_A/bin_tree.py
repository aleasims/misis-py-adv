class BinTree:
    value_type = tuple()

    @classmethod
    def validate(cls, value):
        raise NotImplementedError

    def __init__(self, value, left=None, right=None):
        raise NotImplementedError

    @property
    def value(self):
        raise NotImplementedError

    @value.setter
    def value(self, new_value):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def dfs(self):
        raise NotImplementedError

    @property
    def is_leaf(self):
        raise NotImplementedError


class BinIntTree(BinTree):
    # value_type = ?

    def min(self):
        raise NotImplementedError

    def max(self):
        raise NotImplementedError


def test():
    n0, n1, n2, n3, = [BinIntTree(i) for i in range(4)]
    n4, n5 = BinIntTree(4, n0, n1), BinIntTree(5, n2, n3)
    T = BinIntTree(6, n4, n5)

    assert list(T) == [T, n4, n0, n1, n5, n2, n3]
    assert T.max().value == 6
    assert T.min().value == 0
    assert n1.is_leaf
    assert repr(n2) == '<BinTree 2>'
    n2.value = 15
    assert n2.value == 15


if __name__ == "__main__":
    test()

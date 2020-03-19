class BinTree:
    value_type = tuple()

    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self._value = self.validate(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = self.validate(new_value)

    def __repr__(self):
        return '<{} {}>'.format(self.__class__.__name__,
                                self.value)

    def __iter__(self):
        return self.dfs()

    def dfs(self):
        yield self
        if self.left is not None:
            yield from self.left
        if self.right is not None:
            yield from self.right

    @classmethod
    def validate(cls, value):
        if len(cls.value_type) > 0:
            if not isinstance(value, cls.value_type):
                raise TypeError('Incompatible node value, expected: {}'.format(
                                cls.value_type))
        return value

    @property
    def is_leaf(self):
        return self.left is None and self.right is None


class BinIntTree(BinTree):
    value_type = (int,)

    def min(self):
        return min(self, key=lambda tree: tree.value)

    def max(self):
        return max(self, key=lambda tree: tree.value)


def test():
    n0, n1, n2, n3, = [BinIntTree(i) for i in range(4)]
    n4, n5 = BinIntTree(4, n0, n1), BinIntTree(5, n2, n3)
    T = BinIntTree(6, n4, n5)

    assert list(T) == [T, n4, n0, n1, n5, n2, n3]
    assert T.max().value == 6
    assert T.min().value == 0
    assert n1.is_leaf
    assert repr(n2) == '<BinIntTree 2>'
    n2.value = 15
    assert n2.value == 15


if __name__ == "__main__":
    test()

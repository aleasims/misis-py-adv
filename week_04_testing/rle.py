import itertools


def rle(iterable):
    """Apply run-length encoding to an iterable.

    >>> list(rle(""))
    []
    >>> list(rle("foo"))
    [('f', 1), ('o', 2)]
    """
    for item, g in itertools.groupby(iterable):
        yield item, sum(1 for _ in g)  # Change to sum(1 ...)


def test_rle_foo():
    assert list(rle("foo")) == [('f', 1), ('o', 2)]


if __name__ == "__main__":
    print(list(rle('foo')))
    assert list(rle('foo')) == [('f', 1), ('o', 2)], list(rle('foo'))

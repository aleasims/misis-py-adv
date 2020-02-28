class ReversedIterator:
    def __init__(self, l: list):
        self.l = l
        self.n = len(l) - 1

    def __next__(self):
        if self.n < 0:
            raise StopIteration
        next_elem = self.l[self.n]
        self.n -= 1
        return next_elem

    def __iter__(self):
        return self


class SortingIterator:
    def __init__(self, l):
        self.l = sorted(l)
        self.n = 0
    
    def __next__(self):
        if self.n >= len(self.l):
            raise StopIteration
        next_elem = self.l[self.n]
        self.n += 1
        return next_elem

    def __iter__(self):
        return self


def map(func, iterable): # -> generator
    for item in iterable:
        result = func(item)
        yield result


def fib():
    # 0, 1, 1, 2, 3, 5, 8, 13, ...
    # f_n = f_(n-1) + f_(n-2)
    a, b = 0, 1
    while True:
        yield a
        tmp = a
        a = b
        b = tmp + a


if __name__ == '__main__':
    import itertools
    print(
        list(itertools.islice(fib(), 0, 10))
    )

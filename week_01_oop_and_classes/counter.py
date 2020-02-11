class Counter:
    """Custom Counter implementation."""

    def __init__(self):
        """Constructor of Counter.

        Accepts no parameters:
        initializes an empty Counter anyway.
        """

        self.count = {}  # this attribute collects Counter data

    def __getitem__(self, key):
        """Enable Counter objects values accesed using `counter[...]`."""

        if key not in self.count:
            # In case if `key` not found in counter, simply return 0
            return 0
        
        # Otherwise return count value, which stored in `count` attribute
        return self.count[key]

    def __setitem__(self, key, value):
        """Enable Counter objects values setting using `counter[...] = 1`."""

        self.count[key] = value

    def __str__(self):
        """Return string representation of Counters object."""

        return 'Counter({})'.format(self.count)

    def __add__(self, other):
        """Enable adding Counters object to each other.

        >>> c1 = Counter()
        >>> c2 = Counter()
        >>> c3 = c1 + c2  # new Counter object
        """

        keys = set(self.count) | set(other.count)  # union of keys of counters

        val = Counter()
        for key in keys:
            val[key] = self[key] + other[key]  # using defined __setitem__ and
                                               # __getitem__ here

        return val


if __name__ == "__main__":
    c1 = Counter()
    c1['audi'] += 1
    c1['mercedes'] += 1
    print('c1 = {}'.format(c1))

    c2 = Counter()
    c2['audi'] += 1
    c2['oka'] += 1
    print('c2 = {}'.format(c2))

    c3 = c1 + c2
    print('c1 + c2 = {}'.format(c3))

import csv
import random
from contextlib import contextmanager


def read_file(path):
    data = ''
    try:
        f = open(path, 'r')
        data = f.read()
    finally:
        f.close()
    return data


# same:
def read_file(path):
    data = ''
    with open(path, 'r') as f:
        data = f.read()
    return data


def open_file(path):
    try:
        f = open(path, 'r')
        print('Yielding file')
        yield f
        print('Back in generator')
    except OSError as e:
        print('Something went wrong: {}'.format(e))
    finally:
        print('Closing')
        f.close()


class RandomNumbers:
    def __init__(self, size, start, end):
        self.size = size
        self.start = start
        self.end = end

    def __enter__(self):
        return [random.randint(self.start, self.end)
                for _ in range(self.size)]

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # Nothing to do here
        pass


@contextmanager
def random_numbers(size, start, end):
    yield [random.randint(start, end) for _ in range(size)]


class TmpFile:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.f = open(self.path)
        return self.f

    def __exit__(self, *args):
        self.f.close()


class CsvFile:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        f = open(self.path, 'r')
        table = csv.reader(f)
        f.close()
        return table

    def __exit__(self, *args):
        # Nothing to do here
        pass


if __name__ == "__main__":
    with random_numbers(5, 0, 100) as nums:
        print(nums)

    with RandomNumbers(5, 0, 100) as nums:
        print(nums)

    with TmpFile('test.log') as f:
        print(f.read())

    with CsvFile('test.csv') as table:
        for row in table:
            print(row)

    # f = open_file('./test.log')
    # for item in f:
    #     print('Printing item:')
    #     print(item.read())

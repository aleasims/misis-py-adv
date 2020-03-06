import unittest

from rle import rle


class TestRle(unittest.TestCase):
    def test_rle_empty(self):
        self.assertEqual(list(rle("")), [])

    def test_rle(self):
        expected = [('f', 1), ('o', 2)]
        self.assertEqual(list(rle("foo")), expected)


if __name__ == "__main__":
    unittest.main()

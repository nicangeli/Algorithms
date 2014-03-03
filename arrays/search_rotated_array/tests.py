import unittest
from rotated import SearchRotatedArray

class SearchRotatedTests(unittest.TestCase):
    def setUp(self):
        self.s = SearchRotatedArray()

    def test_bin_search(self):
        arr = [10, 11, 12, 1, 2, 3]
        result = self.s.binary_search(arr, 1)
        self.assertEqual(result, 3)

        arr = [10, 11, 12, 13, 14, 1, 2, 3]
        result = self.s.binary_search(arr, 1)
        self.assertEqual(result, 5)

        result = self.s.binary_search(arr, 10)
        self.assertEqual(result, 0)
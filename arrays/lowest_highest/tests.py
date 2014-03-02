import unittest
from highLow import HighLow

class HighLowTest(unittest.TestCase):

    def setUp(self):
        self.h = HighLow()

    def test_find_low_index(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        result = self.h.find_low_index(arr, 5)
        self.assertEqual(4, result)

        result = self.h.find_low_index(arr, 1)
        self.assertEqual(0, result)

    def test_find_low_index_no_match(self):
        arr = [1, 2, 3, 4, 6]
        result = self.h.find_low_index(arr, 0)
        self.assertEqual(-1, result)

        result = self.h.find_low_index(arr, 5)
        self.assertEqual(-1, result)

    def test_find_low_when_multi_matches(self):
        arr = [1, 1, 1, 2, 2, 2, 3, 6, 8, 9, 9]
        result = self.h.find_low_index(arr, 1)
        self.assertEqual(0, result)

        result = self.h.find_low_index(arr, 9)
        self.assertEqual(9, result)

        result = self.h.find_low_index(arr, 2)
        self.assertEqual(3, result)

    def test_find_high_index(self):
        arr = [1, 2, 3, 3, 3, 6, 8, 10, 10, 10, 10, 22, 22]
        result = self.h.find_high_index(arr, 1)
        self.assertEqual(0, result)

        result = self.h.find_high_index(arr, 3)
        self.assertEqual(4, result)

        result = self.h.find_high_index(arr, 22)
        self.assertEqual(12, result)

    def test_find_high_index_with_no_match(self):
        arr = [1, 2, 5, 7, 9, 10]
        result = self.h.find_high_index(arr, 3)

        self.assertEqual(-1, result)

        result = self.h.find_high_index(arr, 11)
        self.assertEqual(-1, result)

    def test_find_high_low(self):
        arr = [1, 2, 2, 2, 3, 6, 7]
        result = self.h.find_high_low(arr, 2)
        self.assertEqual([1, 3], result)

    def test_find_high_low_no_match(self):
        arr = [1, 2, 3, 5, 6]
        result = self.h.find_high_low(arr, 4)
        self.assertEqual([-1, -1], result)

    def test_find_high_low_one_match_only(self):
        arr = [1, 2, 3, 4]
        result = self.h.find_high_low(arr, 1)
        self.assertEqual([0, 0], result)





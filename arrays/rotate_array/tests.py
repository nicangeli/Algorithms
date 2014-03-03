import unittest
from rotate import RotateArray

class RotateArrayTester(unittest.TestCase):
    def setUp(self):
        self.r = RotateArray()

    def test_rotate(self):
        arr = [1, 10, 20, 0, 59]
        self.r.rotate(arr, 2)
        self.assertEqual(arr, [0, 59, 1, 10, 20])

        arr = [1, 10, 20, 0, 59]
        self.r.rotate(arr, 1)
        self.assertEqual(arr, [59, 1, 10, 20, 0])

        arr = [1, 10, 20, 0, 59]
        self.r.rotate(arr, -1)
        self.assertEqual(arr, [10, 20, 0, 59, 1])

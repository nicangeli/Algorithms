import unittest
from zeros import ZeroMover

class ZeroMoverTest(unittest.TestCase):

    def test_zero_mover_init(self):
        zm = ZeroMover([1, 10, 20, 0, 59, 63, 0, 88, 0])

    def setUp(self):
        self.zm = ZeroMover([1, 10, 20, 0, 59, 63, 0, 88, 0])

    def test_shift_zeroes(self):
        self.zm.shift_zeroes()
        self.assertEquals(self.zm.array, [0, 0, 0, 1, 10, 20, 59, 63, 88])

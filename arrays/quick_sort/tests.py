import unittest
from QuickSort import QuickSort

class QuickSortTester(unittest.TestCase):
    def setUp(self):
        self.qs = QuickSort()

    def test_partition(self):
        arr = [10, 5, 2, 90, 61, 32, 3]
        #pivot point is 10
        #after partition array should be
        #[5, 2, 3, 10, 90, 61, 32]
        result = self.qs.partition(arr, 0, len(arr)-1);
        self.assertEqual(arr[3], 10)
        self.assertTrue(arr[0] <= 10)
        self.assertTrue(arr[1] <= 10)
        self.assertTrue(arr[2] <= 10)
        self.assertTrue(arr[4] >= 10)
        self.assertTrue(arr[5] >= 10)
        self.assertTrue(arr[6] >= 10)

    def test_quick_sort(self):
        arr = [11, 5, 7, 2, 76, 31, 20, 3, 9]
        result = self.qs.quick_sort(arr)
        self.assertEqual(arr, [2, 3, 5, 7, 9, 11, 20, 31, 76])

    def test_quick_sort_on_already_sorted_input(self):
        arr = [1, 2, 3, 4, 5]
        result = self.qs.quick_sort(arr)
        self.assertEqual(arr, result)

    def test_quick_sort_on_partially_sorted_array(self):
        arr = [1, 2, 10, 4, 90, 1001, 23]
        result = self.qs.quick_sort(arr)
        self.assertEqual(result, [1, 2, 4, 10, 23, 90, 1001])

    def test_quick_sort_on_single_element_array(self):
        arr = [9]
        result = self.qs.quick_sort(arr)
        self.assertEqual(result, [9])

    def test_quick_sort_on_two_element_array(self):
        arr = [2, 1]
        result = self.qs.quick_sort(arr)
        self.assertEqual(result, [1, 2])

        arr = [1, 2]
        result = self.qs.quick_sort(arr)
        self.assertEqual(result, [1, 2])



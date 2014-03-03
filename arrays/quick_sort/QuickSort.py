class QuickSort:
    def partition(self, array, low, high):
        if high < low:
            return

        pivot = array[low]
        low_pointer = low
        high_pointer = high

        while low_pointer < high_pointer:
            while array[low_pointer] <= pivot:
                low_pointer += 1
                if low_pointer > len(array)-1:
                    break
            while array[high_pointer] > pivot:
                high_pointer -= 1
            if low_pointer < high_pointer:
                #another check as we increment them inside the condition
                array[low_pointer], array[high_pointer] = array[high_pointer], array[low_pointer]
            else:
                break
        array[low] = array[high_pointer]
        array[high_pointer] = pivot
        return high_pointer

    def recurse(self, array, low, high):
        if high > low:
            pivot = self.partition(array, low, high)
            print "Pivot is: " + str(pivot)
            self.recurse(array, low, pivot-1)
            self.recurse(array, pivot + 1, high)

    def quick_sort(self, array):
        print "Array starts as: " + str(array) 
        self.recurse(array, 0, len(array)-1)
        return array
class HighLow:

    def find_high_low(self, array, target):
        low = self.find_low_index(array, target)
        high = self.find_high_index(array, target)

        return [low, high]

    def find_low_index(self, array, target):
        low = 0
        high = len(array)-1

        while low <= high:
            mid = low + ((high-low)/2)

            if array[mid] < target:
                low = mid +1
            elif array[mid] >= target:
                high = mid -1

        if low >= len(array):
            return -1 
        elif array[low] == target:
            return low
        else:
            return -1

    def find_high_index(self, array, target):
        low = 0
        high = len(array)-1

        while low <= high:
            mid = low + ((high - low) / 2)

            if array[mid] <= target:
                low = mid + 1
            else:
                high = mid -1

        if high >= len(array):
            return -1
        elif array[high] == target:
            return high
        else: 
            return -1



#Please learn how to do proper BDD (like rspec) with Python. Now. 
if __name__ == "__main__":

    highLow = HighLow()
    array = [1, 2, 2, 5, 5, 5, 5, 5, 5, 11];
    print highLow.find_high_low(array, 5)

    """
    a = [1, 2, 5, 5, 5, 7, 8, 9, 10, 11]
    print find_high_index(a, 5)


    a = [1, 2, 5, 5, 5, 7, 8, 9, 10, 11]
    print find_high_index(a, 12)


    a = [1, 2, 5, 5, 5, 7, 8, 9, 9, 10, 11]
    print find_high_index(a, 9)

    a = [1, 2, 3, 5, 7, 8]
    print find_low_index(a, 5)

    a = [1, 2, 2, 5, 7, 8]
    print find_low_index(a, 2)

    a = [1, 2, 3, 5, 5, 5]
    print find_low_index(a, 5)

    a = [1, 2, 3, 5, 5, 5]
    print find_low_index(a, 6)

    a = [1, 2, 3, 4, 5, 5]
    print find_low_index(a, 6)
    """
class SearchRotatedArray:
    def bin_search(self, array, start, end, key):
        if start > end:
            return -1

        mid = start + ((end - start) / 2)

        if array[mid] == key:
            return mid

        if array[start] < array[mid] and key < array[mid] and key >= array[start]:
            return self.bin_search(array, start, mid-1, key)
        elif array[mid] < array[end] and key > arr[mid] and key <= arr[end]:
            return self.bin_search(array, mid+1, end, key)
        elif array[start] > array[mid]:
            return self.bin_search(array, start, mid-1, key)
        elif array[end] < array[mid]:
            return self.bin_search(array, mid+1, end, key)
        return -1

    def binary_search(self, array, key):
        return self.bin_search(array, 0, len(array)-1, key)
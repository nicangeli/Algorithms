class RotateArray:
    def rotate(self, array, n):
        array.reverse()
        first = array[:n]
        first.reverse()
        array[:n] = first
        tail = array[n:]
        tail.reverse()
        array[n:] = tail
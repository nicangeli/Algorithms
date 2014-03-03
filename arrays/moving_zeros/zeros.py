class ZeroMover:
    def __init__(self, array):
        self.array = array

    def shift_zeroes(self):
        if len(self.array) < 1:
            return

        write = len(self.array)-1
        read = len(self.array)-1

        while read >= 0:
            if self.array[read] != 0:
                self.array[write] = self.array[read]
                write -= 1
            read -= 1
 

        while write >= 0:
            self.array[write] = 0
            write -= 1

if __name__ == "__main__":
    zm = ZeroMover([1, 20, 21, 0, 30, 0, 35])
    zm.shift_zeroes()
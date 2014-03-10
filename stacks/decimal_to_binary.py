from Stack import Stack

def divideBy2(decimal):
    s = Stack()
    while decimal > 0:
        remainder = decimal % 2
        s.push(remainder)
        decimal = decimal // 2

    binary = ""
    while not s.isEmpty():
        binary += str(s.pop())

    return binary

if __name__ == "__main__":
    print "100 is: " + divideBy2(100)
    print "200 is: " + divideBy2(200)
from Stack import Stack

def parenthesisChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def genericParenthesisChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "({[":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                popped = s.pop()
                if not matches(popped, symbol):
                    balanced = False
                else:
                    balanced = True
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(popped, symbol):
    #does popped match symbol? popped is one of )}], symbol is one of {([
    closer = {"(": ")", "[": "]", "{": "}"}
    return closer[popped] == symbol


if __name__ == "__main__":
    print parenthesisChecker("((()))")
    print parenthesisChecker("(()")

    print genericParenthesisChecker("(())")
    print genericParenthesisChecker("({})")
    print genericParenthesisChecker("((){}[])")
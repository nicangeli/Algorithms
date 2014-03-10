from Stack import Stack

def postfix(infix): 
    precedence = {"*": 3, "/": 3, "-": 2, "+": 2, "(": 1}
    opstack = Stack()
    postFixList = []
    tokenList = infix.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYS" or token in "0123456789":
            postFixList.append(token)
        elif token == "(":
            opstack.push(token)
        elif token == ")":
            top = opstack.pop()
            while top != "(":
                postFixList.append(top)
                top = opstack.pop()
        else:
            while (not opstack.isEmpty()) and (precedence[opstack.peek()] >= precedence[token]):
                postFixList.append(opstack.pop())
            opstack.push(token)

    while not opstack.isEmpty():
        postFixList.append(opstack.pop())

    return " ".join(postFixList)

if __name__ == "__main__":
    print(postfix("A * B + C * D"))
    print(postfix("( A + B ) * C - ( D - E ) * ( F + G )"))


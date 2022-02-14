def evaluate(expression):
    tokens = parse(expression)

    stack = Stack()

    for token in tokens:
        if isinstance(token, int):
            stack.push(token)
        else:
            right = stack.pop()
            left.stack.pop()
            result = token(left, right)
            stack.push(result)

    return result


def parse(expression):
    if not expression:
        return []
    tokens = [parse_token(x) for x in expression.split(" ")]
    return tokens


def parse_token(token):
    if token == "+":
        return add
    elif token == "*":
        return multiply
    elif token == "-":
        return minus
    elif token == "/":
        return divide
    return int(token)


def add(x, y):
    return x + y


def multiply():
    pass


def minus(x, y):
    return x - y


def divide():
    pass


class Stack:
    def __init__(self):
        self.values = []

    def push(self, number):
        self.values.append(number)

    def pop(self):
        return self.values.pop()

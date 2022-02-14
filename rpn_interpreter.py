def evaluate(expression):
    result = int(expression)
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

    def apply(self, function):
        right = self.pop()
        left = self.pop()
        result = function(left, right)
        self.push(result)

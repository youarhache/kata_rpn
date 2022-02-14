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
    return int(token)

def add():
    pass

def multiply():
    pass
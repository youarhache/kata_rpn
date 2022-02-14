from rpn_interpreter import evaluate
from rpn_interpreter import parse
from rpn_interpreter import add
from rpn_interpreter import multiply
from rpn_interpreter import minus
from rpn_interpreter import divide
from rpn_interpreter import Stack
import pytest


def test_single_value():
    assert evaluate("42") == 42


def test_single_expression():
    assert evaluate("20 2 +") == 22


def test_parse_empty():
    assert parse("") == []


def test_parse_single_value():
    assert parse("45") == [45]


def test_parse_two_numbers():
    assert parse("1 2") == [1, 2]


def test_parse_add():
    assert parse("1 2 +") == [1, 2, add]


def test_parse_multiply():
    assert parse("1 2 *") == [1, 2, multiply]


def test_parse_minus():
    assert parse("1 2 -") == [1, 2, minus]


def test_parse_divide():
    assert parse("1 2 /") == [1, 2, divide]


def test_create_empty_stack():
    stack = Stack()
    assert stack.values == []


def test_push_number_to_stack():
    stack = Stack()
    stack.push(40)
    assert stack.values == [40]


def test_pop_number_from_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    number = stack.pop()
    assert stack.values == [1]
    assert number == 2


def test_apply_add():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.apply(add)
    assert stack.values == [3]


def test_apply_minus():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.apply(minus)
    assert stack.values == [-1]

from rpn_interpreter import evaluate
from rpn_interpreter import parse
from rpn_interpreter import add
from rpn_interpreter import multiply
import pytest
def test_single_value():
    assert evaluate("42") == 42
@pytest.mark.skip
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
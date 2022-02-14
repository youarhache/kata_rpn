from rpn_interpreter import evaluate


def test_single_value():
    assert evaluate("42") == 42

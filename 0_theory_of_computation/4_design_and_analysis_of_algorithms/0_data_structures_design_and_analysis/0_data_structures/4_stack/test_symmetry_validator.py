from use_cases.symmetry_validator import punctuation


def test_valid_punctuation_1():
    assert punctuation("(){()[]{()[]}}")


def test_valid_punctuation_2():
    assert punctuation("((a+b))")


def test_valid_punctuation_3():
    assert punctuation("[a+b]*(x+2y)*{gg+kk}")


def test_valid_punctuation_4():
    assert punctuation("'a+b'")


def test_valid_punctuation_5():
    assert punctuation('"a+b"')


def test_invalid_punctuation_1():
    invalid_code = "[]){()[]{()[]}}"
    try:
        punctuation(invalid_code)
    except Exception as e:
        print(e.args)
        assert e.args[0] == "Stack is empty"


def test_invalid_punctuation_2():
    assert punctuation("))((a+b}{") == False


def test_invalid_punctuation_3():
    assert punctuation("))") == False


def test_invalid_punctuation_4():
    assert punctuation("'a+b") == False


def test_invalid_punctuation_5():
    assert punctuation('"a+b') == False

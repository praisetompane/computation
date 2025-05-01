from stack.symmetry_checking import SymmetryChecker

symmetry_checker = SymmetryChecker()


def test_valid():
    valid_code = "(){()[]{()[]}}"
    print("valid code")
    assert symmetry_checker.lint(valid_code)


def test_invalid():
    invalid_code = "[]){()[]{()[]}}"
    try:
        symmetry_checker.lint(invalid_code)
    except Exception as e:
        print(e.args)
        assert e.args[0] == "Stack is empty"

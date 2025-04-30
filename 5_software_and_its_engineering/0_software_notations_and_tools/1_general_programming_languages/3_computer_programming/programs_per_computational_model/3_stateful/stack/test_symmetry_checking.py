from symmetry_checking import SymmetryChecker

symmetry_checker = SymmetryChecker()
def test_valid():
    valid_code = "(){()[]{()[]}}"
    print("valid code")
    assert symmetry_checker.lint(valid_code)

def test_invalid():
    invalid_code = "[]){()[]{()[]}}"
    print("invalid code - expect Exception('Stack is empty')")
    assert symmetry_checker.lint(invalid_code)


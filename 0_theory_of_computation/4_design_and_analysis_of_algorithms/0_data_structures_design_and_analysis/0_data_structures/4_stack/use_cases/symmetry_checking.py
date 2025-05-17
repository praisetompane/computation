from use_cases.impl.stack import Stack

"""
    general use case: symmetry test
    Performance:
        N = length of _document
        Time = 𝑂(𝑁)
        Space = 𝑂(𝑁)
"""


class SymmetryChecker:
    _document = None
    _opening_parathesis = None
    _opening_curly = "{"
    _opening_round = "("
    _opening_square = "["

    def __init__(self):
        self._opening_parathesis = Stack()

    def lint(self, _document):
        for char in _document:
            if (
                char == self._opening_round
                or char == self._opening_curly
                or char == self._opening_square
            ):
                self._opening_parathesis.push(char)
            if char == "}" and self._opening_parathesis.peek() == self._opening_curly:
                self._opening_parathesis.pop()
            if char == "]" and self._opening_parathesis.peek() == self._opening_square:
                self._opening_parathesis.pop()
            if char == ")" and self._opening_parathesis.peek() == self._opening_round:
                self._opening_parathesis.pop()

        return self._opening_parathesis.is_empty()

import string

"""
    def pangram: a string that contains every letter of the alphabet
"""


def is_pangram(s):
    unique_characters = set(s.lower())
    for c in string.ascii_lowercase:
        if c not in unique_characters:
            return "not pangram"
    return "pangram"


assert is_pangram("We promptly judged antique ivory buckles for the next prize") is True
assert is_pangram("We promptly judged antique ivory buckles") is False

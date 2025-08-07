import string

"""
    def pangram: a string that contains every letter of the alphabet
    Objective: determine if a string is pangram.

    Source: https://www.hackerrank.com/challenges/pangrams/problem
"""


def is_pangram(s):
    # not necessary, this is for set use explicitness
    universe = set(s.lower())
    fixed_domain = set(string.ascii_lowercase)
    return fixed_domain.issubset(universe)


assert is_pangram("We promptly judged antique ivory buckles for the next prize") is True
assert is_pangram("We promptly judged antique ivory buckles") is False

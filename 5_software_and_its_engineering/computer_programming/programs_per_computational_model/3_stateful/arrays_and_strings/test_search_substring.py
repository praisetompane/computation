from arrays_and_strings.search_substring import search_substring


def test_search_substring():
    assert search_substring("SOSSPSSQSSOR") == 3
    assert search_substring("SOSSOT") == 1

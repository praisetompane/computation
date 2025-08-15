from use_cases.order_reversal import reverse_order


def test_reverse_order():
    s1 = "apple"
    assert reverse_order(s1) == "elppa"
    s1 = ""
    assert reverse_order(s1) == ""
    s1 = "racecar"
    assert reverse_order(s1) == "racecar"
    s1 = [1, 2, 3, 4, 5]
    assert reverse_order(s1) == [5, 4, 3, 2, 1]
    s1 = []
    assert reverse_order(s1) == []

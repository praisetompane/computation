"""
Source: https://www.hackerrank.com/challenges/birthday-cake-candles/copy-from/71884152
"""


def count_largest_object_occurrence(ar: list[int]) -> int:
    max_height = 0 if len(ar) == 0 else max(ar)
    return ar.count(max_height)


def main() -> None:
    assert count_largest_object_occurrence([3, 2, 1, 3]) == 2
    assert (
        count_largest_object_occurrence([3, 2, 1, 3, 7, 7, 7, 1, 2, 5, 3, 3, 5, 2, 1])
        == 3
    )

    assert count_largest_object_occurrence([3, 2, 1]) == 1

    assert count_largest_object_occurrence([]) == 0
    assert count_largest_object_occurrence([1]) == 1
    assert count_largest_object_occurrence([1, 2]) == 1

    print("completed successfully")


if __name__ == "__main__":
    main()

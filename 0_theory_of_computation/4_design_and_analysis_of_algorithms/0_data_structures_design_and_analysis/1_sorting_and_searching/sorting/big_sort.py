"""
Given:
    string represented numbers
    example = '1'
Objective:
    sort the list
Constraints:
    n = size of list
    0 <= n <= 2 * 10⁶
Assumptions: None
Performance:
    Time = O(n)
    Space = O(2 * n) = O(n)
        We create a copy of the list
"""


def bigSorting(numbers):
    numbers_sorted = sorted_values(numbers, key=lambda x: int(x))
    return numbers_sorted


unsorted = ["1", "200", "150", "3"]
sorted_values = bigSorting(unsorted)
print(sorted_values)

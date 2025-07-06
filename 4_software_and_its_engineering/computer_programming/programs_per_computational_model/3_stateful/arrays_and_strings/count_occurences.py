"""
Context:
    Given:
        array of integers
            unsorted
        each element appears twice except for one
Objective:
    Find the element that occurs once

Example:
    a = [1,2,3,4,1,2,3]
    unique 4

Assumptions:
    there will always be a lonely integer (i.e. n will always be odd)

Flow
    option 1: 𝑂(𝑁 + 𝑁) = O(2N) = 𝑂(𝑁)
        initialise empty hash occurrences = array_value -> count
        for each value in a
            store count in occurrences
        find entry(key) with only one occurrences
        CHOSE THIS ONE
    Option 2: 𝑂(𝑁𝑙𝑜𝑔𝑁 + 𝑁)
        sort
        return number whose adjacent is not equal to itself

    Option 3: 𝑂(𝑁) + O(1) = 𝑂(𝑁) = WRONG THOUGH
        Since an odd number + odd number = even
              an even number + odd number = even
              sum of n(which odd) is going to be odd

        lonely_integer = sum(a)%2

Constraints:
    1 <= n <= 100: size of the array
    0 <= arr[i] <= 100, where 0 <= i <= 100(n)

Performance
    N = number of elements in array
    Time = O(2 * N)
         = O(N)

Source: https://www.hackerrank.com/challenges/lonely-integer/problem
"""


def lonelyinteger(a):
    occurrences = {}
    for number in a:
        if number in occurrences:
            occurrences[number] += 1
        else:
            occurrences[number] = 1
    for n in occurrences.items():
        if n[1] == 1:
            return n[0]


assert lonelyinteger([1, 1, 2]) == 2

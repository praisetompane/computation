"""

    factorial(6)
    6 * factorial(6 - 1)
    5 * factorial(5 - 1)
    4 * factorial(4 - 1)
    .
    .
    .
    2 * factorial(2 - 1)
    
    runtime = 𝑂(𝑁)

"""


def factorial(n):
    if n < 0:
        return -1
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

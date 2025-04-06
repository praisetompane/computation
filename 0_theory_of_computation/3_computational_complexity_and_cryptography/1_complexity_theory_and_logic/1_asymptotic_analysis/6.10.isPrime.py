""" 
    Complexity
        N == number

        O(N * (N - 1))
        O(N^2 - N)
        => O(N^2)

"""


def isPrime(number):
    if number > 1:
        for i in range(1, number):
            for j in range(2, number):
                if i * j == number:
                    return False
    return True


print(isPrime(4))
print(isPrime(5))

"""
    N == number
    Complexity
        O(N - 1)
        => 𝑂(𝑁)
    prime? == is it divisble by number >= 1 and < number

    Is it divisible by any other number expect 1 and itself
    hence range 2 to number - 1
"""


def isPrime2(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


print(isPrime(4))
print(isPrime(5))

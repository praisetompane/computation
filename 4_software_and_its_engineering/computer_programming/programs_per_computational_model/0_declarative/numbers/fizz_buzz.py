"""
If num % 3 == 0
    Fizz
Else if num % 5 == 0
    Buzz
Else If num % 3 == 0 and num % 5 == 0
    FizzBuzz
"""


def fizz_buzz(lastNumber):
    def evaluate(n):
        if n % 3 == 0 and n % 5 == 0:
            return "FizzBuzz"
        elif n % 5 == 0:
            return "Buzz"
        elif n % 3 == 0:
            return "Fizz"
        else:
            return n

    for n in range(1, lastNumber + 1):
        print(evaluate(n))


def main():
    fizz_buzz(100)


if __name__ == "__main__":
    main()

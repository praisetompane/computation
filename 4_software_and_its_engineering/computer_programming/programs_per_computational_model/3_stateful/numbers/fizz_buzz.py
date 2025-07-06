"""
If num % 3 == 0
    Fizz
Else if num % 5 == 0
    Buzz
Else If num % 3 == 0 and num % 5 == 0
    FizzBuzz
"""


def fizz_buzz(lastNumber):
    print("alternative 2")

    def evaluate(n):
        output = ""
        if n % 3 == 0:
            output += "Fizz"
        if n % 5 == 0:
            output += "Buzz"
        if output == "":
            output = str(n)
        return output

    for n in range(1, lastNumber + 1):
        print(evaluate(n))


class FizzBuzz:
    output = ""
    lastNumber = 1

    def __init__(self, lastNumber):
        self.lastNumber = lastNumber

    def isDivisible(self, number, multiple):
        return number % multiple == 0

    def updateOutput(self, result):
        self.output += result

    def evaluate(self, n):
        if self.isDivisible(n, 3):
            self.updateOutput("Fizz")
        if self.isDivisible(n, 5):
            self.updateOutput("Buzz")
        if self.output == "":
            self.output = str(n)
        return self.output

    def render(self):
        for n in range(1, self.lastNumber + 1):
            self.output = ""
            print(self.evaluate(n))


def main():
    fizz_buzz(100)
    FizzBuzz(100).render()


if __name__ == "__main__":
    main()

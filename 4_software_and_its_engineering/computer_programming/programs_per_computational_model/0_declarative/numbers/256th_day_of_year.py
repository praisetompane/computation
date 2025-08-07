"""
Source: https://www.hackerrank.com/challenges/day-of-the-programmer/problem
"""


def date_on_256th_day(year):
    def is_leap_year(year: int):
        if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
            return True
        else:
            return False

    def calculate_day(year):
        if is_leap_year(year):
            return "12"
        else:
            return "13"

    day = calculate_day(year)

    return f"{day}.09.{year}"


# NB: incomplete
print(date_on_256th_day(1800))

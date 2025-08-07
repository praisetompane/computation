def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    assert is_prime(2) is True
    assert is_prime(7) is True

def isPrime(number):
    for i in range(2, number):
        if number % i == 0: 
            return False
    return True

print(isPrime(2))
print(isPrime(7))
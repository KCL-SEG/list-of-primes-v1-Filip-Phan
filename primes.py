"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(number):
    for i in range(2, int(n+2)+1):
        if (n % i) == 0:
            return False
        else:
            return True

def primes(number_of_primes):
    list = []
    current = 2
    while len(list) < number_of_primes:
        if isPrime(current):
            list.append(current)
        current = current + 1


    return list

import math

def isPrime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True



dest = 10001
counter = 0
n = 3
while counter < dest:
    if isPrime(n):
        counter += 1
    n += 2

print(n)
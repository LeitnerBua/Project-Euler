#!python3

# https://projecteuler.net/problem=7

def power_of_two(n1):
    exp = 1
    while exp <= 512:
        for j in range(100000):
            t = j * (2**exp)
            if n1 == t:
               return j, exp
        exp *= 2


def isPrime(n):
    n1 = n - 1
    prim = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    p = power_of_two(n1)
    if p != None:
        a, b = p
    else:
        return False

    counter = 0
    for number in prim:
        if number == n:
            counter += 1
        else:
            y0 = (number ** a) % n
            if y0 == 1:
                counter += 1
                continue
        for x in range(b):
            y0 = (number ** (a * (2 ** x))) % n
            if y0 == n1:
                counter += 1
                break
    
    if len(prim) == counter:
        return True
    else:
        return False


test_number = 3
counter_prim = 2 # already counted prime number 2 and 3
dest = 10001


while counter_prim <= dest:
    test_number += 2
    prim = isPrime(test_number)
    if prim:
        counter_prim += 1
    

print(test_number)


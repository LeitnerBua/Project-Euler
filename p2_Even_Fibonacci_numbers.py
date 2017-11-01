#!python3

# https://projecteuler.net/problem=2

a = 0
b = 1
dest = 4000000
sumList = []
while b < dest:
    a, b = b, a
    b = a + b
    if b % 2 == 0:
        sumList.append(b)

print(sum(sumList))

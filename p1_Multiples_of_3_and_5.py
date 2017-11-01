#!python3

# https://projecteuler.net/problem=1

sumList = []

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sumList.append(i)

print(sum(sumList))

#!python3

# https://projecteuler.net/problem=6

import math


def sum_of_squares(number):
    sum = 0
    for i in range(number+1):
        sum += math.pow(i, 2)

    return sum


def square_of_sum(number):
    sum = 0
    for i in range(number+1):
        sum += i

    return math.pow(sum, 2)


res = square_of_sum(100) - sum_of_squares(100)
print(res)

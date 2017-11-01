#!python3

# https://projecteuler.net/problem=5


def smallest_multi():
    i = 20
    while True:
        print(i)
        c = 1
        for j in reversed(range(2, 20+1)):
            if not i % j == 0:
                break
            if c == 19:
                return i
            c += 1
        i += 20


smallest_multi()

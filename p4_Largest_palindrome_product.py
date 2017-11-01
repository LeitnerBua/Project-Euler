#!python3

# https://projecteuler.net/problem=4

list_pali = []

for i in reversed(range(100, 999+1)):
    for j in reversed(range(100, 999+1)):
        check_pali = i*j
        rev_pali = str(check_pali)[::-1]
        if check_pali == int(rev_pali):
            list_pali.append(check_pali)

print(max(list_pali))

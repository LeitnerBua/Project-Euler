#!python3

# https://projecteuler.net/problem=2

number_cut = 600851475143
i = 1

# prime number generieren
while i < number_cut:
    if i != 1 and number_cut % i == 0 and i != number_cut:
        print('Primenumber ' + str(i))
        number_cut = number_cut / i
        i = 1
        continue
    i += 1

print('Ergebnis ' + str(number_cut))

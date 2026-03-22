from math import prod

def dell(n, d = 2):
    for d in range(d, int(n ** 0.5) + 1):
        if n % d == 0:
            return [d] + dell(n // d, d)
    return [n]

def proverka(num):
    return num > 1 and all(num % i != 0 for i in range(2, round(num ** 0.5) + 1))

c = 0
for num in range(123_456_790, 124_000_000):
    deliteli = dell(num)

    prostie = [d for d in deliteli if proverka(d)]

    if len(prostie) == 7:
        if prod(prostie) == num and str(sum(prostie)).count('5') > 0 and max(prostie) % 10 == 9:
            print(num, max(prostie))
            c += 1

    if c == 5:
        break
from math import *

def f(x):
    d = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.append(i)
            d.append(x // i)

    return d

c = 0
for x in range(13_475_125, 14_000_000):
    deliteli = f(x)
    prostie = [i for i in deliteli if len(f(i)) == 0 and str(i).count('5') >= 1]

    if len(prostie) == 5:
        # if prostie[0] * prostie[1] * prostie[2] * prostie[3] * prostie[4] == x:
        c += 1
        print(x, max(prostie))
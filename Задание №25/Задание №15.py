from math import *

def f(x):
    d = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.append(i)
            d.append(x // i)

    return d


c = 0
for x in range(3_000_001, 10_000_000):
    d = f(x) # ВСЕ ДЕЛИТЕЛИ
    prostie = [n for n in d if len(f(n)) == 0 and ((str(n).count('1')) == 1 or (str(n).count('3')) == 1)]

    if len(prostie) == 2 and prod(prostie) == x and c < 5:
        print(x, max(prostie))
        c += 1

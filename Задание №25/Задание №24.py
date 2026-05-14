from math import *

def f(num, d = 2):
    for d in range(d, round(num ** 0.5) + 1):
        if num % d == 0:
            return [d] + f(num //d, d)
    return [num]


c = 0
for num in range(8_996_453, 10_000_000):
    d = f(num) # ПРОСТЫЕ
    podh = [pd for pd in d if str(pd).count('3') == 2]

    if len(podh) == 2 and prod(podh) == num:
        # if all(str(pd).count('3') == 2 for pd in d):
            print(num, max(d))
            c += 1

    if c == 5:
        break

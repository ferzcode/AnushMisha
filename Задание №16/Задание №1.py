from functools import *

@lru_cache(None)
def f(n):
    if n >= 21: return f(n - 5) + 3480
    if n < 21: return 10 * (g(n - 9) - 30)


@lru_cache(None)
def g(n):
    if n >= 264685: return n / 20 + 33
    if n < 264685: return g(n + 9) - 2


for n in range(270000, 0, -1):
    g(n)

for n in range(0, 270000):
    f(n)


print(f(675))

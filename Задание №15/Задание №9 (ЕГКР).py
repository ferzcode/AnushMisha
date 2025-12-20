def f(x, y):
    return (78125 != (y + 4 * x)) or ((A > x) and (A > y))

for A in range(0, 100000):
    if all(f(x, y) for x in range(1, 20000) for y in range(1, 10000)):
        print(A)
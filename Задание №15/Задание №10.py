def f(x, y):
    return (x * y < A) or (x < 7 * y) or (343 < x)

for A in range(100_000, 0, -1):
    if all(f(x, y) for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
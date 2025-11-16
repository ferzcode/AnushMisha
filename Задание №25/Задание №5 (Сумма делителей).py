def f(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sum(d)

c = 0
for x in range(500_001, 1000_000):
    R = f(x)
    if R % 10 == 6 and c < 5:
        c += 1
        print(x, R)
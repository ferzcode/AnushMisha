def f(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return d

c = 0
for x in range(902715, 1000_000):
    delit = f(x)
    d5 = [a for a in delit if a % 10 == 5 and a != 5]

    if len(d5) > 0 and c < 6:
        print(x, min(d5))
        c += 1
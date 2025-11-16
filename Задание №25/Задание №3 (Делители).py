def f(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return d

c = 0
for x in range(700001, 1000_000):
    deliteli = f(x)
    d = [a for a in deliteli if a % 10 == 7 and a != 7]
    if len(d) > 0 and c < 5:
        c += 1
        print(x, min(d))
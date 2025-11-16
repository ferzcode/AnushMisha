def f(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return d


c = 0
for x in range(860_001, 1000_000):
    deliteli = f(x)

    M = 0
    if len(deliteli) > 0:
        M = max(deliteli) - min(deliteli)

    if M % 100 == 18 and c < 5:
        c += 1
        print(x, M)
def f(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return d


c = 0
for x in range(799_999, 1, -1):
    deliteli = f(x)

    M = 0
    if len(deliteli) > 0:
        M = max(deliteli) - min(deliteli)

    if M % 23 == 0 and M != 0 and c < 5:
        c += 1
        print(x, M)
def f(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return d

c = 0
for x in range(1000_001, 2000_0001):
    deliteli = f(x) # Здесь лежат все делители set()
    M = 0
    if len(deliteli) > 0:
        M = min(deliteli) + max(deliteli)

    if M % 10 == 6 and c < 5:
        print(x, M)
        c += 1
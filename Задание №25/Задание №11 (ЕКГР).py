def f(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return d

c = 0
for num in range(13_200_000, 14_000_000):
    d = f(num)
    prostie = [j for j in d if len(f(j)) == 0]
    M = 0 if len(prostie) < 2 else max(prostie) + min(prostie)

    if M > 30000 and M % 100 == 55 and c < 7:
        print(num, M)
        c += 1
def pr(x):
    z = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            z.append(i)
            z.append(x // i)
    return z


c = 0
for i in range(1324728, 1400000):
    k = pr(i)
    d = [i for i in k if len(pr(i)) == 0]
    if len(d) == 2 and d[0] * d[1] == i and str(d[0]).count('5') == 1 and str(d[1]).count('5') == 1 and c < 5:
        c += 1
        print(i, max(d))





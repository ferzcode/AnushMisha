def f(x):
    d = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.append(i)
            d.append(x // i)

    return d

def pros(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

c = 0
for x in range(13_475_126, 13_481_000):
    delit = f(x)
    prostie = [i for i in delit if pros(i)]

    if len(prostie) == 5:
        print(x,  prostie)



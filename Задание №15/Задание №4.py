def f(x):
    P = 25 <= x <= 64
    Q = 40 <= x <= 115
    A = a1 <= x <= a2

    return (P <= ((Q and (not A)) <= (not P)))

r = [] # ЗДЕСЬ ЛЕЖАТ ДЛИНЫ НАШИХ A
d = [24.9, 25, 25.1, 63.9, 64, 64.1, 39.9, 40, 40.1, 114.9, 115, 115.1]
# d = [y for x in [25, 64, 40, 115] for y in [x - 0.1, x, x + 0.1]]

for a1 in d:
    for a2 in d:
        if a2 >= a1 and all(f(x) == 1 for x in d):
            r.append(a2 - a1)

print(round(min(r)))
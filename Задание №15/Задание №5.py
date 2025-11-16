def f(x):
    P = 215 <= x <= 264
    Q = 221 <= x <= 294
    A = a1 <= x <= a2

    return not(P <= (((not A) and Q) <= (not P)))

r = []
d = [214.9, 215, 215.1, 263.9, 264, 264.1, 220.9, 221, 221.1, 293.9, 294, 294.1]

for a1 in d:
    for a2 in d:
        if a2 >= a1 and all(f(x) == 0 for x in d):
            r.append(a2 - a1)
print(round(min(r)))
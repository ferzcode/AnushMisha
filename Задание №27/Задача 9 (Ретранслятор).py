from math import *

clA = [[], [], []]

for s in open('27A_22076.txt'):
    x, y = [float(p) for p in s.split()]

    if 20 < x < 25 and 0 < y < 5:
        clA[0].append([x, y])
    if 25 < x < 30 and y < 0:
        clA[1].append([x, y])
    if y > 10:
        clA[2].append([x, y])

def AntiCenter(cl):
    m = []
    for p1 in cl:
        s = sum(dist(p1, p2) for p2 in cl)
        m.append([s, p1])
    return max(m)[1]

Anti1 = AntiCenter(clA[0])
Anti2 = AntiCenter(clA[1])
Anti3 = AntiCenter(clA[2])

m = []
for p1 in clA[0] + clA[1] + clA[2]:
    summa = dist(p1, Anti1) + dist(p1, Anti2) + dist(p1, Anti3)
    m.append([summa, p1])
Retranlator = max(m)[1]


print(int(Retranlator[0] * 10000), int(Retranlator[1] * 10000))





















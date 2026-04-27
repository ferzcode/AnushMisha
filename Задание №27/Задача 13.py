from math import *

clA = [[], []]

def plotnost(cl):
    m = []
    for p1 in cl:
        s = sum([p2[-1] for p2 in cl if dist(p1[:2], p2[:2]) <= 1])
        m.append([s, p1])
    return max(m)[1]

for s in open("27A (3).txt"):
    x, y, t = s.replace(',','.').split()
    x, y, t = float(x), float(y), int(t)
    if y < -3:
        clA[0].append([x, y, t])
    elif y > -3:
        clA[1].append([x, y, t])

pl1 = plotnost(clA[0])
pl2 = plotnost(clA[1])

Px  = (pl1[0] + pl2[0]) / 2
Py = (pl1[1] + pl2[1]) / 2
print(abs(Px * 10000), abs(Py * 10000))
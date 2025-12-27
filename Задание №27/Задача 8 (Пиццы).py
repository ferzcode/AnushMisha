# y = 2x - 0.4

from math import *

clA = [[], []]
for s in open('27.11.A_20206.txt'):
    x, y = [float(p) for p in s.split()]

    if y < 2 * x - 0.4: clA[0].append([x, y])
    else: clA[1].append([x, y])


clB = [[], [], [], []]
for s in open('27.11.B_20206.txt'):
    x, y = [float(p) for p in s.split()]

    if y < - 3 * x + 34:
        clB[0].append([x, y])
    if y > - 3 * x + 34 and y > 3 * x - 26:
        clB[1].append([x, y])
    if y < 3 * x - 26 and y > 0.5 * x - 1:
        clB[2].append([x, y])
    if y > - 3 * x + 34 and y < 0.5 * x - 1:
        clB[3].append([x, y])



def Center(cl):
    m = []
    for p1 in cl:
        s = sum(dist(p1, p2) for p2 in cl)
        m.append([s, p1])
    return min(m)[1]


Center1 = Center(clA[0])
Center2 = Center(clA[1])
Px = int(((Center1[0] + Center2[0]) / 2) * 10000)
Py = int(((Center1[1] + Center2[1]) / 2) * 10000)

Center1 = Center(clB[0])
Center2 = Center(clB[1])
Center3 = Center(clB[2])
Center4 = Center(clB[3])

Px2 = int(((Center1[0] + Center2[0] + Center3[0] + Center4[0]) / 4) * 10000)
Py2 = int(((Center1[1] + Center2[1] + Center3[1] + Center4[1]) / 4) * 10000)


print(Px, Py)
print(Px2, Py2)



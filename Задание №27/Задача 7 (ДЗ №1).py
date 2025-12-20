from math import dist

def Center(cl):
    m = []
    for p1 in cl:
        s = sum(dist(p1, p2) for p2 in cl)
        m.append([s, p1])
    return min(m)[1]

cl1 = []
cl2 = []
for s in open('Задание №1А.txt'):
    x, y = [float(p) for p in s.replace(',', '.').split()]

    if 84 < y < 90:
        cl1.append([x, y])
    if 94 < y < 100:
        cl2.append([x, y])

Center1 = Center(cl1)
Center2 = Center(cl2)

P1 = Center2[0] + Center2[1]
P2 = Center1[0] + Center1[1]
print(P1 * 10000, P2 * 10000)

Q1 = dist(Center1, [0, 0])
Q2 = dist(Center2, [0, 0])

# print(Q1, Q2)

Qx = Center1[0]
Qy = Center2[1]

# МИНИМАЛЬНАЯ ИЗ АБСЦИСС

PX = min(Center1[0], Center2[0])

max_dist = 0
for p in cl1:
    max_dist = max(max_dist, dist(p, Center1))
for p in cl2:
    max_dist = max(max_dist, dist(p, Center2))


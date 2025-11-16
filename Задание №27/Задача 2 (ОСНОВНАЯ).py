from math import *

def Center(kl):
    m = []
    for p1 in kl:
        s = sum(dist(p1, p2) for p2 in kl)
        m.append([s, p1])

    return min(m)[1]



kl1 = []
kl2 = []
kl3 = []

for s in open('27_B_23284.txt'):
    x, y = [float(p) for p in s.split()]

    if 4 < x < 10:
        kl1.append([x, y])
    if 14 < x < 19.5:
        kl2.append([x, y])
    if 19.5 < x < 26:
        kl3.append([x, y])

center1 = Center(kl1)
center2 = Center(kl2)
center3 = Center(kl3)

distance12 = dist(center1, center2)
distance23 = dist(center2, center3)
distance13 = dist(center1, center3)

Q1 = min(distance12, distance23, distance13)
Q2 = max(distance12, distance23, distance13)

print(abs(int(Q1 * 10000)))
print(abs(int(Q2 * 10000)))
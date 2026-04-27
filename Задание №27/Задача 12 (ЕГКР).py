from math import *
def Center(cl):
    m = []
    for p1 in cl:
        s = 0
        for p2 in cl:
            s += dist(p1, p2)
        m.append([s, p1])
    return min(m)[1]

cl1 = []
cl2 = []
cl3 = []

c = 0
for s in open('27_B_28946.txt'):
    x, y = map(float, s.replace(',', '.').split())
    c += 1
    if 25 < x < 30:
        cl1.append([x, y])
    if 15 < x < 25 and 13 < y < 20:
        cl2.append([x, y])
    if y > 25:
        cl3.append([x, y])


c1 = Center(cl1)
c2 = Center(cl2)
c3 = Center(cl3)

B1 = 0
for p in cl1:
    if c1[0] - 0.9 < p[0] < c1[0] + 0.9 and c1[1] - 0.9 < p[1] < c1[1] + 0.9:
        B1 += 1

print(B1)
B2 = abs(c2[1] - c3[1])
print(B2 * 10000)





















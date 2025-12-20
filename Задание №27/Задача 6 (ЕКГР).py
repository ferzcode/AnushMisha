from math import *

def Center(cl):
    m = []
    for p1 in cl:
        s = sum(dist(p1, p2) for p2 in cl)
        m.append([s, p1])
    return min(m)[1]

cl1 = []
cl2 = []
for s in open('27_A_25364.txt'):
    x, y = [float(p) for p in s.replace(',', '.').split()]

    if 2 < x < 6 and 4 < y < 8:
        cl1.append([x, y])
    if 5 < x < 9 and 10 < y < 14:
        cl2.append([x, y])

Center1 = Center(cl1) # [
Center2 = Center(cl2)

P1 = min(dist(Center1, [1.0, 1.0]), dist(Center2, [1.0, 1.0]))
P2 = max(dist(Center1, [1.0, 1.0]), dist(Center2, [1.0, 1.0]))
print(P1 * 10000, P2 * 10000)

cl1 = []
cl2 = []
cl3 = []
for s in open('27_B_25364.txt'):
    x, y = [float(p) for p in s.replace(',', '.').split()]

    if 10 < y < 15:
        cl1.append([x, y])
    if 16 < y < 22:
        cl2.append([x, y])
    if 22 < y < 30:
        cl3.append([x, y])

Center1 = Center(cl1)
Center2 = Center(cl2)
Center3 = Center(cl3)

Q1 = 0
Q2 = 0
for p1 in cl1:
    if dist(p1, Center1) <= 1.2:
       Q1 += 1
    if dist(p1, Center1) <= 0.75:
       Q2 += 1
print(Q1, Q2)
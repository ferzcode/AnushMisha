from math import *

def isolate(kl):
    m = []
    for p1 in kl: # [10, 20, 30]
        c = 0 # Кол-во точек в единичной окрестности
        for p2 in kl: # [10, 20, 30]
            if dist(p1, p2) <= 1:
                c += 1
                # 0     1    2
        m.append([c, -p1[1], p1])
    return min(m)[2]


kl1 = []
kl2 = []
kl3 = []
kl4 = []

for s in open('27A_20294.txt'):
    x, y = [float(p) for p in s.split()]

    if y > 0 and x < 0:
        kl1.append([x, y])
    if y > 2 and 2 < x < 5:
        kl2.append([x, y])
    if 3.5 < x < 8 and -3 < y < 2:
        kl3.append([x, y])
    if x < 1 and y < 0:
        kl4.append([x, y])

is1 = isolate(kl1)
is2 = isolate(kl2)
is3 = isolate(kl3)
is4 = isolate(kl4)

Px = (is1[0] + is2[0] + is3[0] + is4[0]) / 4
Py = (is1[1] + is2[1] + is3[1] + is4[1]) / 4

print(abs(Px) * 100000)
print(abs(Py) * 100000)
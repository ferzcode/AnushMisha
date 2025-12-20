from math import *

def plot(cl):
    m = []
    for p in cl:
        k = len([p1 for p1 in cl if dist(p,p1)<=1])
        m.append(k)
    return sum(m)/len(m)

def plotnost(kl):
    m = [] # Количество
    c = 0
    for p1 in kl:
        c = 0
        for p2 in kl:
            if dist(p1, p2) <= 1:
                c += 1
        m.append(c)

    return sum(m) / len(m)


kl1 = []
kl2 = []
kl3 = []
kl4 = []

for s in open('27A_20295.txt'):
    x, y = [float(p) for p in s.split()]

    if y > 0 and x < 0:
        kl1.append([x, y])
    if y > 2 and 2 < x < 5:
        kl2.append([x, y])
    if 3.5 < x < 8 and -3 < y < 2:
        kl3.append([x, y])
    if x < 1 and y < 0:
        kl4.append([x, y])

pl1 = plotnost(kl1)
pl2 = plotnost(kl2)
pl3 = plotnost(kl3)
pl4 = plotnost(kl4)

print(min(pl1, pl2, pl3, pl4) * 100000)
print(((pl1 + pl2 + pl3 + pl4) / 4) * 100000)
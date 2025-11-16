from math import dist

def distance(kl1, kl2):
    m = []
    for p1 in kl1: # p1 = [x, y]
        for p2 in kl2: # p2 = [x, y]
            m.append(dist(p1, p2))
    return min(m) # Меняем min на max чтобы найти максимальное растояние между точками


kl1 = []
kl2 = []
kl3 = []

for s in open('27_B_23571.txt'):
    x, y = [float(p) for p in s.split()]

    if 8 < x < 20 and 8 < y < 13.5:
        kl1.append([x, y])
    if 14 < x < 20 and 13.5 < y < 21:
        kl2.append([x, y])
    if 22 < x < 30:
        kl3.append([x, y])


rast1 = distance(kl1, kl2)
rast2 = distance(kl2, kl3)
rast3 = distance(kl1, kl3)

Q1 = min(rast1, rast2, rast3)
Q2 = max(rast1, rast2, rast3)

print(int(Q1 * 10000))
print(int(Q2 * 10000))

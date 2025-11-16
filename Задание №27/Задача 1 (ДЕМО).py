from math import *

def Center(kl):
    m = []
    for p1 in kl:
        s = sum(dist(p1, p2) for p2 in kl)
        #         0   1
        m.append([s, p1])

    return min(m)[1]

# def Center(kl):
#     m = []
#     for x1, y1 in kl:
#         summa = 0
#         for x2, y2 in kl:
#             summa += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#         m.append([summa, x1, y1])
#
#     c, x, y = min(m) # Ищет минимум по сумме
#     return x, y


kl1 = []
kl2 = []
kl3 = []

for s in open('27_B_17882.txt'):
    x, y = [float(p) for p in s.split()]

    if x < 3 and y < 4:
        kl1.append([x, y])
    if y > 6 and 2 < x < 5:
        kl2.append([x, y])
    if x > 5:
        kl3.append([x, y])



#                        0  1
center1 = Center(kl1) # [x, y]
center2 = Center(kl2) # [x, y]
center3 = Center(kl3) # [x, y]

Px = (center1[0] + center2[0] + center3[0]) / 3
Py = (center1[1] + center2[1] + center3[1]) / 3
#
# print(center1)
# print(center2)
#
#
print(Px * 10000, Py * 10000)











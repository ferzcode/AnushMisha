from math import *

k1 = 70
N1 = 1025
i1 = ceil(log(N1, 2))
V1 = k1 * i1

k2 = 4
N2 = 26
i2 = ceil(log(N2, 2))
V2 = k2 * i2

V = ceil((V1 + V2) / 8)
Vodin = 24 * 1024 * 1024 / 131072

print(Vodin - V)
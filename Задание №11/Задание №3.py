from math import *

for N in range(10000000, 1, -1):
    k = 246
    i = ceil(log(N, 2))
    V1 = ceil((k * i) / 8)

    if V1 * 703_569 <= 77 * 1024 * 1024:
        print(N)
        break
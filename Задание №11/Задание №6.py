from math import *

for x in range(1, 1000000):
    N = 33 + 33 + x
    k = 21
    i = ceil(log(N, 2))
    V1 = ceil((k * i) / 8)

    if V1 * 1300 <= 25 * 1024:
        print(x)

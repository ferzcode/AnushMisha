from math import *

for N in range(1, 10000000):
    k = 172
    i = ceil(log(N, 2))
    V1 = ceil((k * i) / 8)

    if V1 * 356_984 >= 54 * 1024 * 1024:
        print(N)
        break
from math import *
# более - >
# менее - <
# не менее - >=
# не более - <=

for k in range(1, 10000):
    N = 10 + 52 + 500
    i = ceil(log(N, 2))
    V1 = ceil((k * i) / 8)

    if V1 * 45877 > 49 * 1024 * 1024:
        print(k)
        break
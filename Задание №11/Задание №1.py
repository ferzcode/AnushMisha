from math import *

k = 317
N = 4090 + 10

i = ceil(log(N, 2))
V1 = ceil((k * i) / 8)

print((V1 * 262_144) / (1024 * 1024))
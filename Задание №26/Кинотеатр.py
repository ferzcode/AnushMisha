f = open('26_20910.txt')
N, M, K = map(int, f.readline().split())

min_ryad = [M + 1] * (K + 1)
for i in range(N):
    ryad, mesto = map(int, f.readline().split())

    if ryad < min_ryad[mesto]:
        min_ryad[mesto] = ryad

    # min_ryad[mesto] = min(ryad, min_ryad[mesto])

max_ryad = 0 # Самый дальний ряд найденный
best_mesto = 0 # Номер места в найденной паре для ряда

for mesto in range(1, K):
    ryad = min(min_ryad[mesto], min_ryad[mesto + 1]) - 1

    if ryad > max_ryad:
        max_ryad = ryad
        best_mesto = mesto
    if ryad == max_ryad and mesto < best_mesto:
        best_mesto = mesto

print(max_ryad, best_mesto)
def check(A):
    for dx in range(-1000, 1000):
        for dy in range(-1000, 1000):
            x = 12126 + dx
            y = 12126 + dy

            f = (3 * x + 4 * y != 84882) or (x < y) or (A < x)
            if f == 0: return 0
    return 1

for A in range(12125, 10 ** 8, 1):
    if check(A) == 1:
        print(A)
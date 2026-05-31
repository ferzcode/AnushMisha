def check(A):
    for dx in range(-1000, 1000):
        for dy in range(-1000, 1000):
            x = 535 + dx
            y = 1605 + dy

            f = (x * y < A) or (3 * x < y) or (535 <= x)
            if f == 0:
                return 0
    return 1

for A in range(10**8, 0, -1):
    if check(A) == 1:
        print(A)
# maxi = 0
for x in range(2, 2025):
    num = 5 ** 2025 + 5 ** 200 - x

    c4 = 0
    while num > 0:
        if num % 5 == 4:
            c4 += 1
        num //= 5

    if c4 == 199:
        print(x)

    # maxi = max(maxi, c4)
# print(maxi)
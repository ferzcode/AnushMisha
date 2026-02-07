n = 220 # minimum

c = 0
while c < 5:
    number = n * (n + 1) * (n + 2)

    if 10 ** 7 <= number < 10 ** 8:
        print(number, 3 * n + 3)
        c += 1
    n += 10
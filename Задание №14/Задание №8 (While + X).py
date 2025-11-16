for x in range(1, 2031):
    number = 3 ** 100 - x
    c0 = 0
    while number > 0:
        if number % 3 == 0:
            c0 += 1
        number //= 3

    if c0 == 5:
        print(x)

from re import fullmatch

for x in range(0, 10 ** 10, 1984):
    if fullmatch(r'[2468]9[0-9]23[0-9][0-9]*23[13579][02468]', str(x)):
        print(x, x // 1984)
def chet(n):
    new = ''
    while n > 0:
        new = str(n % 4) + new
        n //= 4
    return new

otvet = []
for N in range(1, 1000):
    cher = chet(N)
    if N % 4 == 0:
        cher = cher + cher[-2:]
    else:
        cher += chet((N % 4) * 2)

    R = int(cher, 4)
    if R < 261:
        otvet.append()
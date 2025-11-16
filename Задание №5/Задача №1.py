def tri(n):
    new = ''
    while n > 0:
        new = str(n % 3) + new
        n //= 3
    return new


otvet = []
for N in range(167, 1000):
    triple = tri(N)

    # summa = triple.count('3') * 3 + triple.count('2') * 2 + triple.count('1') * 1
    summa = sum(map(int, triple))

    if summa % 9 == 0:
        triple = triple + '2'
    else:
        triple = triple + tri(summa % 9)

    R = int(triple, 3)
    otvet.append(R)
print(min(otvet))
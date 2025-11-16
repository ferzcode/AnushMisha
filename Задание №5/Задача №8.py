import abc


def f(N):
    new = ''
    while N > 0:
        new = str(N % 6) + new
        N //= 6
    return new

otvet = []
for N in range(1, 10000):
    six = f(N)

    # summa = sum(map(int, six))
    summa = sum([int(i) for i in six])

    if summa % 5 == 0:
        six = six.replace('0', '*')
        six = six.replace('3', '0')
        six = six.replace('*', '3')
        six = '11' + six
    else:
        six = six + '44'
        six = six[0] + '05' + six[3:]
    R = int(six, 6)

    if R == 1504:
        otvet.append(N)
print(max(otvet))

    # if R > 1500:

        # otvet.append(R)
# print(min(otvet))


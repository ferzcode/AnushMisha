otvet = []
for N in range(1, 10000):
    b = bin(N)[2:]

    if N % 2 == 0:
        b += '0'
    else:
        b += '1'

    if b.count('1') % 3 == 0:
        b = '11' + b[2:]
    else:
        b = '10' + b[2:]

    R = int(b, 2)
    if R <= 37:
        otvet.append(N)
print(max(otvet))
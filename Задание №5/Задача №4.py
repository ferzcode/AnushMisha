otvet = []
for N in range(2, 10000):
    b = bin(N)[2:]
    b = b[:-1] + b[1] * 2

    R = int(b, 2)
    if R > 92:
        otvet.append(N)
print(min(otvet))
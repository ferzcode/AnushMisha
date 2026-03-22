otvet = []
for N in range(1, 10000):
    binary = bin(N)[2:]

    if N % 3 == 0:
        binary = binary + binary[-3:]
    else:
        ostatok = bin((N % 3 ) * 3)[2:]
        binary += ostatok

    R = int(binary, 2)
    if R == 127:
        otvet.append(N)
print(max(otvet))
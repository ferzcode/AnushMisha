otvet = []
for N in range(4, 1000):
    b = bin(N)[2:]

    if N % 2 == 0:
        b = b + b[-2:]
    else:
        b = b + b[-3:]

    R = int(b, 2)
    if R > 256:
        otvet.append(N)
print(min(otvet))
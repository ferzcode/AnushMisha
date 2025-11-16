a = set()
for N in range(10, 1000):
    b = bin(N)[2:]
    b = b[1:]
    index = b.find('1')
    if index != -1:
        b = b[index:]

    R = int(b, 2)
    R = N - R

    a.add(R)
print(len(a))
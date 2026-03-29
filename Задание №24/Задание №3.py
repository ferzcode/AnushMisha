f = open('Задание 24 (1).txt').readline()
k = 0
m = 0

for i in range(len(f)):
    if (f[i - 1] == 'F' and f[i] == 'S') or \
            (f[i - 1] == 'S' and f[i] == 'W') or \
            (f[i - 1] == 'W' and f[i] == 'Y') or \
            (f[i - 1] == 'Y' and f[i] == 'F'):
        k += 1
    else:
        k = 1

    m = max(m, k)
print(m)            
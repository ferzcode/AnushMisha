f = open('Задание №3.txt').readline()
c = ''
m = 0

for r in range(len(f)):
    c += f[r]

    while c.count('C') > 2 or c.count('D') > 2:
        c = c[1:]

    m = max(m, len(c))
print(m)
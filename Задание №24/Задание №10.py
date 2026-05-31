f = open('Задание №6.txt').readline()
m = 0
c = ''

for r in range(len(f)):
    c += f[r]

    while c.count('S') > 35 or (c.count('0') + c.count('2') + c.count('4') + c.count('6') + c.count('8')) > 1:
        c = c[1:]

    if c.count('S') == 35 and c[0] in '02468' and (c.count('0') + c.count('2') + c.count('4') + c.count('6') + c.count('8')) == 1:
        m = max(m, len(c))
print(m)
f = open('Задание №5.txt').readline()
m = 100000000
c = ''

for r in range(len(f)):
    c += f[r]

    if c[-1] in 'AEIOUY':
        while c.count('20') >= 26:
            if c.count('20') == 26:
                m = min(m, len(c))
            c = c[1:]
        c = ''

print(m)



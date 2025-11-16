from string import *

for x in printable[1:22]:
    for y in printable[:13]:
        number = int(f'{x}23{x}5', 22) - int(f'67{y}9{y}', 13)
        if number % 57 == 0:
            print(number // 57, x, y)

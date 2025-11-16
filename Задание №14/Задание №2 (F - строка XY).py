from string import *

for x in printable[:15]:
    for y in printable[:17]:
        number = int(f'123{x}5', 15) + int(f'67{y}9', 17)
        if number % 131 == 0:
            print(number // 131, y)
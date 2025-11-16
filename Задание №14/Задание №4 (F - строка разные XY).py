from string import *

# print(printable[:25])
# print(printable[:11])

# ВЫБИРАЕМ ПО МИНИМАЛЬНОЙ СИСТЕМЕ СЧИСЛЕНИЯ

for x in printable[:11]:
    for y in printable[:11]:
        number = int(f'7{y}23{x}5', 25) + int(f'67{x}9{y}', 11)
        if number % 131 == 0:
            print(number // 131)
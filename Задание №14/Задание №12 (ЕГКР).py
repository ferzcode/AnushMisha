from string import printable

for x in printable[:27]:
    num = int(f'472{x}215', 27) + int(f'92{x}538', 27)
    if num % 26 == 0:
        print(num // 26)
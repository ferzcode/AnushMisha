summa = 0
kolvo = 0

for stroka in open():
    s = [int(x) for x in stroka.split()]

    if ... :
        summa += sum(s)
        kolvo += len(s)

print(summa // kolvo)
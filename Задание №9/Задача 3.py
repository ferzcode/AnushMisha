# Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
# Определите наибольший номер строки таблицы, для чисел которой выполнены оба условия:
#
# - в строке есть одно число, которое повторяется трижды, остальные три числа различны;
# - повторяющееся число строки больше, чем среднее арифметическое её неповторяющихся чисел.
#
# В ответе запишите только число.

nomer = 0
for s in open('../Задача №3.txt'):
    nomer += 1
    a = [int(x) for x in s.split()]

    triple = [x for x in a if a.count(x) == 3] # ЭТИХ 3
    odinochki = [x for x in a if a.count(x) == 1] # ЭТИХ 3

    srarifm = sum(odinochki) / len(odinochki) if len(odinochki) > 0 else 0

    if len(triple) == 3 and len(odinochki) == 3:
        if triple[0] > srarifm:
            print(nomer)
            break
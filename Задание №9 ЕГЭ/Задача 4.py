# Откройте файл электронной таблицы, содержащей в каждой строке восемь натуральных чисел.
#
# Определите наибольший номер строки таблицы, содержащей числа, для которых выполнены оба условия:
#
# – в строке есть ровно три числа, каждое из которых повторяется дважды, остальные числа без повторений;
# – квадрат разности наибольшего и наименьшего из повторяющихся чисел строки больше удвоенной суммы квадратов её неповторяющихся чисел.
#
# В ответе запишите только число.


nomer = 0

for s in open('../Задача №4.txt'):
    a = [int(x) for x in s.split()]
    nomer += 1

    tridvajdi = [x for x in a if a.count(x) == 2] # ЭТО ПРОВЕРИТЬ НА ДЛИНУ = 6
    nepovtorki = [x ** 2 for x in a if a.count(x) == 1] # ЭТО ПРОВЕРИТЬ НА ДЛИНУ = 2

    kvrazn = (max(tridvajdi) - min(tridvajdi)) ** 2 if len(tridvajdi) > 0 else 0
    sumkvadratov = sum(nepovtorki) * 2 if len(nepovtorki) > 0 else 0

    if len(tridvajdi) == 6 and len(nepovtorki) == 2:
        if kvrazn > sumkvadratov:
            print(nomer)
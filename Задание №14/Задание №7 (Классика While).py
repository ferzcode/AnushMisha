number = 30 * 36 ** 231 + 18 * 6 ** 101 - 3 * 36 ** 45 - 2357

c = 0
while number > 0:
    cifra = number % 36 # ЦИФРА ИЗ НОВОЙ 36 ЗАПИСИ ЧИСЛА
    if (cifra % 5 == 0) + (cifra % 3 == 0) == 1:
        c += 1
    number //= 36
print(c)
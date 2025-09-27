# ПРОСТОЙ ПЕРЕБОР ПОДРЯД

a = [1, 2, 3, 4, 50, 100, 80]
for i in range(len(a)):
    print(a[i])

# ПАРА ЧИСЕЛ (СОСЕДНИМИ)

a = [1, 2, 3, 4, 50, 100, 80]
for i in range(len(a) - 1):
    print(a[i], a[i + 1])

# ТРОЙКА ЧИСЕЛ (СОСЕДНИХ)

a = [1, 2, 3, 4, 50, 100, 80]
for i in range(len(a) - 2):
    print(a[i], a[i + 1], a[i + 2])

# ПАРА ЧИСЕЛ (РАЗЛИЧНЫЕ ЭЛЕМЕНТЫ)

a = [1, 2, 3, 4, 50, 100, 80]

for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        print(a[i], a[j])
        
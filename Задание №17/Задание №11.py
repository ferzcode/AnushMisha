def usl1(num1, num2, num3):
    return (num1 % 40 == 15) + (num2 % 40 == 15) + (num3 % 40 == 15)

def usl2(num1, num2, num3):
    return (num1 % 7 == 0) + (num2 % 7 == 0) + (num3 % 7 == 0) # 0 1 2 3


otvet = []
a = [int(i) for i in open('17_23903.txt')]

summa = 0
for i in range(len(a) - 2):
    if usl1(a[i], a[i + 1], a[i + 2]) == 2 and usl2(a[i], a[i + 1], a[i + 2]) <= 2:
        if a[i] % 40 != 15:
            otvet.append(a[i])
        if a[i + 1] % 40 != 15:
            otvet.append(a[i + 1])
        if a[i + 2] % 40 != 15:
            otvet.append(a[i + 2])

print(len(otvet))
print(sum(otvet))
s = open('Задание №24.txt').readline()
countA = 0
left = 0

otvet = 1000000000000000000

for right in range(len(s)):
    if s[right] == 'A':
        countA += 1

    while countA == 2024:
        otvet = min(otvet, right - left + 1)

        if s[left] == 'A':
            countA -= 1
        left += 1

print(otvet)
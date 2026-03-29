#  содержит только буквы латинского алфавита A, C, D, F и O. Определите максимальное количество идущих подряд троек символов вида
# согласная + любая буква + гласная
# Например, для строки ACCADAADD ответом будет число 2 (ACCADAADD).

s = open("24-253.txt").readline()
ans = 1
s = s.replace("C", "D").replace("A", "O").replace("F", "D")
for L in range(len(s) - 1):
    for R in range(L + ans - 1, len(s)):
        t = s[L:R + 1]
        if len(t) % 3 == 0:
            if any(t[i] + t[i + 2] != "DO" for i in range(0, len(t), 3)):
                break

            if all(t[i] + t[i + 1] + t[i + 2] == "DDO" for i in range(0, len(t), 3)):
                if len(t) >= ans:
                    ans = len(t)
                    print(ans // 3, t)
s = open("Задание 24 (1).txt").readline()
ans = 4
for L in range(len(s)):
    for R in range(L+ans -1,len(s)):
        t = s[L:R+1]

        # 0123
        # FSWY
        if any("FSWY".find(t[i + 1]) != ("FSWY".find(t[i]) + 1) % 4 for i in range(len(t) - 1)):
            break
        if "FSWY" in t:
            if len(t) >= ans:
                ans = len(t)
print(ans,t)

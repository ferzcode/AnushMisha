def f(num, d = 2):
    for d in range(d, round(num ** 0.5) + 1):
        if num % d == 0:
            return [d] + f(num // d, d)
    return [num]


c = 0
for num in range(456790, 1000000):
    d = sorted(set(f(num))) # ПРОСТЫЕ ДЕЛИТЕЛИ

    M = d[0] + d[1] + d[-2] + d[-1] if len(d) >= 4 else 0

    if M % 114 == 39:
        c += 1
        print(num, M)

    if c == 5:
        break

def trian(n, m, k):
    return n + m > k and n + k > m and m + k > n

def f(x):
    return (trian(A, 7, x) <= ((max(x + 5, 14) <= 27) == (not(trian(36, 21, x)))))

for A in range(1, 1000):
    if all(f(x) == 1 for x in range(1, 1000)):
        print(A)
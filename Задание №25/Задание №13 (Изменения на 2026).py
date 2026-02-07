from math import log

k111 = [x for x in range(222, 1_000_000, 222) if all(c not in '13579' for c in str(x))]
st5 = [5 ** x for x in range(1, 15)]

a = []
for chislo1 in k111:
    for chislo2 in st5:
        if chislo1 + chislo2 > 1_000_000:
            a.append([chislo1 + chislo2, log(chislo2, 5)])

for chislo, stepen in sorted(a)[:5]:
    print(chislo, stepen)
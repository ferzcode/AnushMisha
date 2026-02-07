from math import *

n103 = [x for x in range(103, 1_000_000, 103) if x % 2 != 0]
st3 = [3 ** x for x in range(1, 15)]

a = []
for chislo1 in n103:
    for chislo2 in st3:
        if 10 ** 5 <= (chislo1 + chislo2) < 10 ** 6 and all(c != '1' for c in str(chislo1 + chislo2)):
            a.append([chislo1 + chislo2, log(chislo2, 3)])


for chislo, stepen in sorted(a)[:5]:
    print(chislo, stepen)
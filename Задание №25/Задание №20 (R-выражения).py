from re import fullmatch

# amp = [str(2 ** x) for x in range(0, 20)]

for x in range(0, 10 ** 10, 1432):
    if fullmatch(r'8902[0-9][0-9]^(1|2|4|8|16|32|64|128|256|512|1024|2048|4096|8192|16384|32768|65536|131072|262144|524288)$', str(x)):
        print(x, x // 1432)

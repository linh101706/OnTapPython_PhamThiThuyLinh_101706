import math
a = float(input())
if 0 < a < 0.01: 
    tong = 0
    n = 0
    while True:
        dieukien = 1 / (2 * n + 1)
        if dieukien < a: break
        tong += 1 / math.factorial(2 * n + 1)
        n += 1
    print("S = {0:.2f}".format(tong))
else: print("ERROR")

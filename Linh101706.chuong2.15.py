import math
ep, x = map(float, input().split())
if 0 < ep < 1:
    tong = 1
    n = 1
    while True:
        dieukien = (x**n) / math.factorial(n)
        if (dieukien < ep): break
        tong += dieukien
        n += 1
    print("e^x = {0}".format(tong))
else: print("ERROR")
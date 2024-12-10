import math
def can(x, n):
    if n == 1: return math.sqrt(x)
    return math.sqrt(x + can(x, n - 1))
x, n = input().split()
x = float(x)
n = int(n)
tong = 1 + can(x , n)
print("S = {0:.2f}".format(tong))
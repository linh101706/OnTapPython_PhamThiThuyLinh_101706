import math
n = int(input())
tong = sum([math.factorial(i) for i in range (1, 2 * n + 2, 2)])
print("S = {0}".format(tong))
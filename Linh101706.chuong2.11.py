import math
n = int(input())
tong = sum([math.factorial(i) for i in range (1,n+1)])
print("S = {0}".format(tong))
import math
n = int(input())
tong = sum([1 / math.factorial(i) for i in range(1, 2 * n + 2, 2)])
print("S = {0}".format(tong))
tong2 = 0
n2 = 0
while (tong2 <= 1000):
    n2 += 1
    tong2 += n2
print("So nguyen duong n nho nhat sao cho 1 + 2 +3 +...+ n > 1000 la: n = {0}".format(n2))
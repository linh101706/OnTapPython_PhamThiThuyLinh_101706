x, n = input().split()
x = float(x)
n = int(n)
tong = sum([x**i for i in range(0, n + 1)])
print("S = {0:.2f}".format(tong))


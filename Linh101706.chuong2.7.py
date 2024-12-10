n = int(input())
tong = sum([1/(i * ( i + 1)) for i in range(1, n + 1)])
print("S = {0:.2f}".format(tong))
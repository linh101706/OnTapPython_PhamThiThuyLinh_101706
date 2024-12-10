n = int(input())
tong = sum([i * 3 for i in range(1, n + 1)]) #líst comprhension
print("S = {0}".format(tong))
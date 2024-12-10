def isNguyenTo(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) +1): #hoac xai math.sqrt(x) + 1 cung duoc
        if n % i == 0: return False
    return True
n = int(input())
for i in range (1, n + 1):
    if isNguyenTo(i): print("{0}".format(i), end = " ")

# Cach 1: Xai de quy
# def giaithua(n):
#     if n == 0 or n == 1: return 1
#     else: return n * giaithua(x -1)
# Cach 2: Xai vong lap
def giaithua(n):
    kq = 1
    for i in range(1, n +1):
        kq *= i
    return kq
n = int(input())
print(giaithua(n))
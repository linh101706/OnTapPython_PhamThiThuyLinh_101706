# Cach 1:
# def isHoanHao(n):
#     tong = sum(i for i in range(1, n) if n % i == 0)
#     return tong == n
# Cach 2:
def isHoanHao(n):
    if n < 2: return False
    tong = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            tong += i
            if i != n // i: tong += n // i
    return tong == n
a, b = map(int, input().split())
dayHoanHao = [str(i) for i in range(a, b + 1) if isHoanHao(i)]
print(" ".join(dayHoanHao))
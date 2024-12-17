def nhap(m):
    a = []
    for i in range(m):
        hang = list(map(int, input().split()))
        a.append(hang)
    return a
def tinhTong(A):
    chinh = 0
    phu = 0
    n = len(A)
    for i in range(n):
        chinh += A[i][i]
        phu += A[i][n - i - 1]
    return chinh, phu
n = int(input())
A = nhap(n)
chinh, phu = tinhTong(A)
print(chinh)
print(phu)
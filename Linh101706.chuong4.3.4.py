def nhap(m, n):
    a = []
    for i in range(m):
        hang = list(map(int, input().split()))
        a.append(hang)
    return a
def xuat(C):
    for hang in C:
        print(" ".join(map(str, hang)))
def cong(A, B):
    m = len(A)
    n = len(A[0])
    C = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C
m, n = map(int, input().split())
A = nhap(m, n)
B = nhap(m, n)
C = cong(A, B)
xuat(C)
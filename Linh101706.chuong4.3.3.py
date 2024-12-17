def nhap(m, n):
    a = []
    for i in range(m):
        hang = list(map(int, input().split()))
        a.append(hang)
    return a
def nhan(A,B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    C = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
def xuat(C):
    for hang in C:
        print(" ".join(map(str, hang)))
m, n, p = map(int, input().split())
A = nhap(m, n)
B = nhap(n, p)
C = nhan(A, B)
xuat(C)
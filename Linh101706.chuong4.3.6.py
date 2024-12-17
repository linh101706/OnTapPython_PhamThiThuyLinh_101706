def nhap(m):
    a = []
    for i in range(m):
        hang = list(map(int, input().split()))
        a.append(hang)
    return a
def isDoiXung(A):
    n = len(A)
    for i in range(n):
        for j in range(i , n):
            if A[i][j] != A[j][i]: return "NO"
    return "YES"
n = int(input())
A = nhap(n)
print(isDoiXung(A))
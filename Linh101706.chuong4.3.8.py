def nhap(m):
    a = []
    for i in range(m):
        hang = list(map(int, input().split()))
        a.append(hang)
    return a
def kiemTra(A):
    n = len(A)
    tren = True
    duoi = True
    for i in range(n):
        for j in range(n):
            if i > j and A[i][j] != 0: tren = False
            if i < j and A[i][j] != 0: duoi = False
    if tren: return "UPPER TRIANGLE" 
    elif duoi: return "LOWER TRIANGLE" 
    else: return "NONE"
n = int(input())
A = nhap(n)
print(kiemTra(A))
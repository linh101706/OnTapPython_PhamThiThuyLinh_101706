def nhap(m, n):
    a = []
    for i in range(m):
        hang = list(map(int, input().split()))
        a.append(hang)
    return a
def timHang(A):
    B = []
    for i in range(len(A)):
        if sum(A[i]) % 7 == 0:
            B.append(i + 1)
    return B
m, n = map(int, input().split())
A = nhap(m, n)
B = timHang(A)
if B: 
    for hang in B: print(hang)
else: print("NO")
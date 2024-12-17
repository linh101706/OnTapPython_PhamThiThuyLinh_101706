def nhap(m, n):
    a = []
    for i in range(m):
        hang = list(map(int, input().split()))
        a.append(hang)
    return a
def tim(A, k):
    dem = 0
    for hang in A:
        dem += hang.count(k)
    return dem
m, n, k = map(int, input().split())
A = nhap(m, n)
print(tim(A, k))
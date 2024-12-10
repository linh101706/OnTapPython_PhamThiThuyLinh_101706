def tim(a, trai, phai, k):
    return a[trai:phai+1].count(k)
n, q = map(int, input().split())
s = input()
mang = []
for i in range(q):
    trai, phai, c = input().split()
    trai, phai = int(trai) - 1, int(phai) - 1
    mang.append((trai, phai, c))
kq = []
for i in mang:
    trai, phai, c = i
    kq.append(tim(s, trai, phai, c))
print('\n'.join(map(str, kq)))
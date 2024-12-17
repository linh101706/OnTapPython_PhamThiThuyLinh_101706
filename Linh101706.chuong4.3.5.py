def nhap(m, n):
    a = []
    for i in range(m):
        hang = list(map(int, input().split()))
        a.append(hang)
    return a
def tinhTBC(a):
    tong = 0
    dem = 0
    for hang in a:
        tong += sum(hang)
        dem += len(hang)
    return tong / dem
def tim(a, tbc):
    kq = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] > tbc:
                kq.append((a[i][j], i + 1, j + 1))
    return kq
def xuat(tbc, kq):
    print(f"{tbc:.2f}")
    for gt, hang, cot in kq:
        print(f"{gt} {hang} {cot}")
m, n = map(int, input().split())
a = nhap(m, n)
tbc = tinhTBC(a)
xuat(tbc, tim(a, tbc))
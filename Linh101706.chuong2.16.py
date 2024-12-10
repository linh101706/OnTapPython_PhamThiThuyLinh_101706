import math
def isTamGiac(a, b, c):
    if a + b > c and a + c > b and b + c > a: return True
    else: return False
def tinhDienTich(a, b, c):
    p = tinhChuVi(a, b, c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
def tinhChuVi(a, b, c):
    return a + b + c
a, b, c = map(int, input().split())
if isTamGiac(a, b, c): print("{0:.2f} {1:.2f}".format(tinhChuVi(a, b, c), tinhDienTich(a, b, c)))
else: print("Khong la tam giac")

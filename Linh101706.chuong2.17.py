import math
def isTamGiac(a, b, c):
    if a + b > c and a + c > b and b + c > a: return True
    else: return False
def tinhDienTich(a, b, c):
    p = tinhChuVi(a, b, c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
def tinhChuVi(a, b, c):
    return a + b + c
def tinhDoDai(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
x1, y1, x2, y2, x3, y3 = map(int, input().split())
a = tinhDoDai(x1, y1, x2, y2)
b = tinhDoDai(x2, y2, x3, y3)
c = tinhDoDai(x3, y3, x1, y1)
if isTamGiac(a, b, c): print("{0:.2f} {1:.2f}".format(tinhChuVi(a, b, c), tinhDienTich(a, b, c)))
else print("Khong la tam giac")

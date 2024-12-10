def tinhTongChuSo(n):
    tong = 0
    while n > 0:
        chuSo = n % 10 #lay chuSo cuoi cung
        tong += chuSo
        n //= 10 #loai bo chuSo cuoi cung
    return tong
n = int(input())
print(tinhTongChuSo(n))
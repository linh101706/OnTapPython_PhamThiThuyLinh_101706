def chuyenSangHexa(n):
    if n == 0: return "0"
    soHex = "0123456789ABCDEF"
    chuoiSo = ""
    while n > 0:
        du = n % 16
        chuoiSo = soHex[du] + chuoiSo
        n = n // 16
    return chuoiSo
n = int(input())
print(chuyenSangHexa(n))
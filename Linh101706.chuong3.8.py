def chuyenSangBin(n):
    if n == 0: return
    else:
        du = n % 2
        chuyenSangBin(n // 2)
        print(du, end = '')
n = int(input())
chuyenSangBin(n)
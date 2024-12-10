def RLE(s):
    if not s: return ""
    chuoiCon = []
    dem = 1
    kyTuTruoc = s[0]
    for i in range(1, len(s)):
        if s[i] == kyTuTruoc: dem += 1
        else:
            chuoiCon.append("{0}{1}".format(kyTuTruoc, dem))
            kyTuTruoc = s[i]
            dem = 1
    chuoiCon.append("{0}{1}".format(kyTuTruoc, dem))
    return ''.join(chuoiCon)
n = int(input())
kq = []
for i in range(n):
    s = input()
    kq.append(RLE(s))
for i in kq:
    print(i)
class SinhVien:
    def __init__(self):
        self.ten = ""
        self.ma = 0
        self.diemToan = 0.0
        self.diemTriet = 0.0
        self.diemLTC = 0.0
        self.diemTrungBinh = 0.0
    def xuat(self):
        print("{0} {1} {2:.2f} {3:.2f} {4:.2f} {5:.2f}".format(self.ma, self.ten, self.diemToan, self.diemTriet, self.diemLTC, self.diemTrungBinh))
    def nhap(self):
        self.ten, self.ma, self.diemToan, self.diemTriet, self.diemLTC = input().split()
        self.ma = int(self.ma)
        self.diemToan, self.diemTriet, self.diemLTC = map(float, (self.diemToan, self.diemTriet, self.diemTrungBinh))
        self.diemTrungBinh = (self.diemToan + self.diemTriet + self.diemLTC) / 3
n = int(input())
ds = []
for i in range(n):
    sv = SinhVien()
    sv.nhap()
    ds.append(sv)
dem = 0
print("Danh sach sinh vien hoc lai")
for i in ds:
    # if (i.diemToan < 4 and i.diemTriet < 4) or (i.diemToan < 4 and i.diemLTC < 4) or (i.diemTriet < 4 and i.diemLTC <4):
    if sum(1 for diem in [i.diemToan, i.diemTriet, i.diemLTC] if diem < 4) >= 2:
        i.xuat()
        dem += 1
print("Danh sach nay co {0} sinh vien phai hoc lai".format(dem))

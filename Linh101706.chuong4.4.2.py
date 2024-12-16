class Sach:
    def __init__(self):
        self.ten = ""
        self.soTrang = 0
        self.giaTien = 0
        self.giaTienTrungBinh = 0
    def xuat(self):
        return ("{0} {1} {2} {3:.2f}".format(self.ten, self.soTrang, self.giaTien, self.giaTienTrungBinh))
    def nhap(self):
        self.ten, self.soTrang, self.giaTien = input().split()
        self.soTrang = int(self.soTrang)
        self.giaTien = int(self.giaTien)
        if self.giaTien != 0:
            self.giaTienTrungBinh = round(self.soTrang / self.giaTien, 2)
n = int(input())
ds = []
for i in range(n):
    sach = Sach()
    sach.nhap()
    ds.append(sach)
ds.sort(key=lambda x: (x.giaTienTrungBinh, x.ten))
with open("sach.txt","w") as file:
    file.write("Danh sach sau khi sap xep:\n")
    for sach in ds:
        file.write(sach.xuat() + "\n")


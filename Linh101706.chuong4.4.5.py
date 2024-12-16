class NhanVien:
   
    def __init__(self):
        self.name = ""
        self.ma = 0
        self.hs = 0
        self.pc = 0

    def nhap(self):
        self.name,self.ma,self.hs,self.pc = input().split()
        self.ma = int(self.ma)
        self.hs = float(self.hs)
        self.pc = int(self.pc)
        self.luong = self.hs * 2000000 + self.pc

    def xuat(self):
        print("{0} {1} {2:.2f} {3} {4:.2f}".format(self.ma, self.name,self.hs, self.pc, self.luong))

n = int(input())
ds = []
for i in range(n):
    nv = NhanVien()
    nv.nhap()
    ds.append(nv)
ds.sort(reverse= True, key=lambda x:x.luong)

print("Danh sach nhan vien da sap xep:", n)
for nv in ds:
    nv.xuat()
class Sach:
    def __init__(self, ten="", soTrang=0, giaTien=0): 
        self.ten = ten 
        self.soTrang = soTrang 
        self.giaTien = giaTien
    def xuat(self):
        return "{0} {1} {2}".format(self.ten, self.soTrang, self.giaTien)
    def chuyenChuoi(s):
        a = s.split()
        ten = a[0]
        soTrang = int(a[1])
        giaTien = int(a[2])
        return Sach(ten, soTrang, giaTien)
ds = []
with open("sach.txt","r") as file:
    for i in file:
        ds.append(Sach.chuyenChuoi(i.strip()))
locDS = [i for i in ds if i.giaTien > 100000 and i.soTrang < 200]
with open("ketqua.txt","w") as file:
    for i in locDS:
        file.write(i.xuat() + "\n")
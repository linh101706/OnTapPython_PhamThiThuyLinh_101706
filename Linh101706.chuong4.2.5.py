def demHoa(s):
    dem = 0
    for i in range(len(s)):
        if s[i].isupper(): dem += 1
    return dem
def demThuong(s):
    dem = 0
    for i in range(len(s)):
        if s[i].islower(): dem += 1
    return dem
def demSo(s):
    dem = 0
    for i in range(len(s)):
        if  s[i].isdigit(): dem += 1
    return dem
s = input()
print("{0:<15}{1:<15}{2:<15}".format("Dem hoa", "Dem thuong", "Dem so"))
print("{0:<15}{1:<15}{2:<15}".format(demHoa(s), demThuong(s), demSo(s)))
# can trai, giua, phai: <, ^, >. {:<10}{:^10}{:>10}
import re
def chuanHoaChuoi(s):
    so = list(map(int, re.findall(r'\d+',s)))
    chu =  re.findall(r'\D+',s)
    so.sort()
    chuoi =""
    for i in range(len(so)):
        chuoi += chu[i]+ str(so[i])
    chuoi += ''.join(chu[len(so):])
    return chuoi
s = input()
print(chuanHoaChuoi(s))
s = input().strip().split()
chuanHoa = ' '.join(s)
if chuanHoa: # if len(chuanHoa) > 0
    chuanHoa = chuanHoa[0].upper() + chuanHoa[1:]
print(chuanHoa)
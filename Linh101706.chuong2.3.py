import math
a, b, c = map(float,input().split())
if a == 0: 
    print("ERROR")
else:
    denta = b**2 - 4 * a * c
    if denta < 0: print("VN")
    elif denta == 0: print("Phuong trinh co nghiem kep:\nx = {0:.2f}".format(-b / (2 * a)))
    else:
        x1 = (- b - math.sqrt(denta))/(2 * a)
        x2 = (-b + math.sqrt(denta))/(2 * a)
        if x1 < x2: print("Phuong trinh co 2 nghiem phan biet:\nx1 = {0:.2f}, x2 = {1:.2f}".format(x1, x2))
        else: print("Phuong trinh co 2 nghiem phan biet:\nx1 = {0:.2f}, x2 = {1:.2f}".format(x2, x1))
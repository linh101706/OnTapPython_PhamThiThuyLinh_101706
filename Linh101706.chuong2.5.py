a1, b1, c1 = map(float,input().split())
a2, b2, c2 = map(float,input().split())
d = a1 * b2 - b1 * a2
dx = c1 * b2 - b1 * c2 
dy = a1 * c2 - c1 * a2 
if d == 0:
    if dy == 0 and dx == 0: print("VSN")
    else: print("VN")
else:
    x = dx / d
    y = dy / d
    print("He phuong co nghiem duy nhat:\nx = {0:.2f}, y = {1:.2f}".format(x, y))
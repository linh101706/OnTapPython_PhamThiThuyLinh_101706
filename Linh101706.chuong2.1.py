a,b = map(float,input().split())
if a != 0 : x = -b/a
else:
    if b == 0: x = "VN"
    else: x = "VSN"
print(x)

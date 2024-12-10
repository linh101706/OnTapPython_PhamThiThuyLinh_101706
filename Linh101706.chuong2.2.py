a, b = map(float,input().split())
if a > 0 : print("x > {0:.2f}".format(-b/a))
elif a == 0:
    if b > 0: print("VSN (luon dung)")
    else: print("Vo li")
else: print("x < {0:.2f}".format(-b/a))
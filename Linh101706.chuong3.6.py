# Cach 1:
# def fibonaci(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return fibonaci(n - 1) + fibonaci(n - 2)
# Cach 2:
def fibonaci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        a, b = 0, 1
        for _ in range (2, n+1):
            a, b = b, a + b
        return b
n = int(input())
tong = 0
x = 0
for i in range(1, n +1):
    x = fibonaci(i)
    print (x, end = " ")
    tong += x
print("\nS = {0}".format(tong))
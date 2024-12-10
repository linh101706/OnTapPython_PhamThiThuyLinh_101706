def UCLN(a, b):
    while b:
        a, b = b, a % b
    return a
def BCNN(a, b):
    return (a * b) // UCLN(a, b)
a, b = map(int, input().split())
print(BCNN(a, b))
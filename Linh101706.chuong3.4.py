def UCLN(a, b):
    while b: #Trong python cac gia tri khac 0 duoc coi la True, gia tri 0 duoc coi la False
        a, b = b, a % b
    return a
a, b = map(int, input().split())
print(UCLN(a, b))
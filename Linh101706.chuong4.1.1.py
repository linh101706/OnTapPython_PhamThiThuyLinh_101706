# def tim(a, k): 
#     for i in a:
#         if i == k: return True;
#     return False
def tim(a, k): 
    trai = 0
    phai = len(a) - 1
    while(trai <= phai):
        m = (trai + phai) // 2
        if k == a[m]: return True
        else:
            if k > a[m]: trai = m + 1
            else: phai = m - 1
    return False
n , k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
b = list(map(int, input().split()))
for i in b:
    if tim(a, i): print("YES")
    else: print("NO")
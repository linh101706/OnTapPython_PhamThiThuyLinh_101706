s = map(int, input().split(','))
chuoi = ([str(i) for i in s if i % 2 != 0])
print(' '.join(chuoi))


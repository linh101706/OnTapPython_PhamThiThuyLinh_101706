s = input()
xuLy = set()
for i in range(len(s)):
    if s[i] not in xuLy:
        print("{0}:{1}".format(s[i],s.count(s[i])))
        xuLy.add(s[i])
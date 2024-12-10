import re 
s = input()
print(max(map(int, re.findall(r'\d+',s))))

# re.findall(r'.', 'abc\ndef')  # ['a', 'b', 'c', 'd', 'e', 'f'] bat ky cai nao ngoai tru xuong dong
# re.findall(r'\d', 'abc123')  # ['1', '2', '3'] - chu so
# re.findall(r'\D', 'abc123')  # ['a', 'b', 'c'] - khong phai chu so
# re.findall(r'\w', 'abc_123')  # ['a', 'b', 'c', '_', '1', '2', '3'] - chu/sp/ gach duoi
# re.findall(r'\W', 'abc_123!@#')  # ['!', '@', '#'] - nguoc lai cua \w
# re.findall(r'\s', 'a b\tc\nd')  # [' ', '\t', '\n']
# re.findall(r'\S', 'a b\tc\nd')  # ['a', 'b', 'c', 'd']
# \d*: Khớp với 0 hoặc nhiều chữ số.
# \d?: Khớp với 0 hoặc 1 chữ số.
# \d{n}: Khớp với chính xác n chữ số.
# \d{n,m}: Khớp với ít nhất n và nhiều nhất m chữ số.

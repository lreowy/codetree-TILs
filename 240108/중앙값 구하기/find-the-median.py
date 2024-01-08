s = input().split()
a = int(s[0])
b = int(s[1])
c = int(s[2])

if a>b:
    if b>c:
        mid = b
    else:
        mid = c
if b>c:
    if a>c:
        mid = a
    else:
        mid = c
if c>a:
    if a>b:
        mid = a
    else:
        mid = b

print(mid)
s = input().split()
a = int(s[0])
b = int(s[1])
c = int(s[2])

if a>b:
    if b>c:
        mid = b
    elif b<c:
        mid = c
if b>c:
    if a>c:
        mid = a
    elif c>a:
        mid = c
if c>a:
    if a>b:
        mid = a
    elif b>a:
        mid = b

print(mid)
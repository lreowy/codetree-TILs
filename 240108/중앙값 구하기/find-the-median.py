s = input().split()
a = int(s[0])
b = int(s[1])
c = int(s[2])

if a>b and a>c:
    if b>c:
        mid = b
    else:
        mid = c
elif b>a and b>c:
    if a>c:
        mid = a
    else:
        mid = c
elif c>a and c>b:
    if a>b:
        mid = a
    else:
        mid = b
print(mid)
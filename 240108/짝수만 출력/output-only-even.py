s = input().split()
a = int(s[0])
b = int(s[1])

while a<=b:
    if a % 2 == 0:
        print(a, end=" ")
    a += 1
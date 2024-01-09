s = input().split()
a = int(s[0])
b = int(s[1])
i = 1
while True:
    i += 1
    if a%i ==0 and b%i ==0:
        continue
    else:
        break
if i == 2:
    print(0)
else:
    print(1)
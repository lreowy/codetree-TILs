s = input().split()
a = int(s[0])
b = int(s[1])
i = 2
while True: 
    if a%i ==0 and b%i ==0:
        i += 1
    else:
        break
if i == 2:
    print(0)
else:
    print(1)
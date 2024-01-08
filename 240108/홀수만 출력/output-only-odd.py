s = input().split()
a = int(s[0])
b = int(s[1])

for i in range(b+1):
    if i>=a:
        if i%2==1:
            print(i,end=" ")
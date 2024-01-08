s = input().split()
a = int(s[0])
b = int(s[1])
ans = 0
for i in range(a,b+1,1):
    if i%6 == 0 and i%8 != 0:
       ans += i
print(ans)
s = input().split()
a = int(s[0])
b = int(s[1])
ans = a
arr = []
cnt = 0
ssum =0
while True:
    arr.append(ans%b)
    ans= ans//b
    if ans <= 1:
        break
count = [0] * 10

for elem in arr:
    count[elem] += 1

for i in range(len(count)):
    ssum += count[i]**2

print(ssum)
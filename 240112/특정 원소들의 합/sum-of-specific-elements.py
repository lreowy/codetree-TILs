arr2 = []
for i in range(4):
    arr = list(map(int,input().split()))
    arr2.append(arr)
ans = 0
for i in range(0,4):
    for j in range(i+1):
        ans += arr2[i][j]
print(ans)
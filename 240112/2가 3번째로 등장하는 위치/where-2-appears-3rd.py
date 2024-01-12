n = int(input())
arr = list(map(int,input().split()))
count = 0
idx = 0
for i in range(n):
    idx += 1
    if arr[i] == 2:
        count += 1
    if count == 3:
        print(idx)
        break
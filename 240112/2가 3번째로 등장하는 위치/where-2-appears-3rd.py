n = int(input())
arr = list(map(int,input().split()))
count = 0
idx = -1
for i in range(len(arr)):
    if arr[i] == 2:
        idx += 1
        count += 1
    if count == 3:
        print(idx+1)
        break
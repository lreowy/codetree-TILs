n = int(input())
arr = list(map(int,input().split()))
min_ = 100

for i in range(n):
    if i == 0:
        continue
    if min_ > arr[i] - arr[i-1]:
        min_ = arr[i]-arr[i-1]
print(min_)
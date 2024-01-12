n = int(input())

count = [0] * 10
arr = list(map(int, input().split()))
for elem in arr:
    count[elem] += 1
for i in range(1,len(count)):
    print(count[i])
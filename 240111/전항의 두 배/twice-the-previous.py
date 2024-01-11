arr = [0,0,0,0,0,0,0,0,0,0,0]
s = input().split()
arr[0] = int(s[0])
arr[1] = int(s[1])

for i in range(10):
    if i>=2:
        arr[i] = arr[i-1] + 2*arr[i-2]

for j in range(10):
    print(arr[j],end=" ")
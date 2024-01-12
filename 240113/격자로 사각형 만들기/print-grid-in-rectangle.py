n = int(input())
arr =[]
for i in range(n):
    a = [0] * n
    arr.append(a)
for i in range(n):
    for j in range(n):
        if i==0:
            arr[i][j] = 1
        if j==0:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i][j-1] + arr[i-1][j]
        print(arr[i][j],end=" ")
    print()
arr2_1 = []
arr2_2 = []
n,m = list(map(int,input().split()))
for i in range(n):
    arr1_1 = list(map(int,input().split()))
    arr2_1.append(arr1_1)
for i in range(n):
    arr1_2 = list(map(int,input().split()))
    arr2_2.append(arr1_2)

for i in range(n):
    for j in range(m):
        if arr2_1[i][j] == arr2_2[i][j]:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()
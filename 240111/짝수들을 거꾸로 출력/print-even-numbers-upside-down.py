num_list = []
n = int(input())
s = input().split()
for i in range(n):
    num_list.append(int(s[i]))

for k in range(n-1,-1,-1):
    if num_list[k]%2==0:
        print(num_list[k],end=" ")
n = int(input())
num_list = []
for i in range(n):
    s = int(input())
    num_list.append(s)

for i in range(len(num_list)):
    ans = int(num_list[i])
    if ans % 2 ==1 and ans %3 ==0:
        print(ans)
n = int(input())
cnt = 0
ans = n
i = 1
while True:
    ans = int(ans/i)
    cnt += 1
    if ans <= 1:
        break
    i += 1

print(cnt)
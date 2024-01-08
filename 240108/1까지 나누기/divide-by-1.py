n = int(input())
cnt = 0
ans = n
i = 1
while True:
    ans = int(ans/i)
    i += 1
    cnt += 1
    if ans < i:
        break

print(cnt)
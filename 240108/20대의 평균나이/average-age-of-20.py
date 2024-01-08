a = 0
cnt = 0
while True:
    n = int(input())
    if n < 20 or n>29:
        break
    a += n
    cnt += 1
    
print(f"{a/cnt:.2f}")
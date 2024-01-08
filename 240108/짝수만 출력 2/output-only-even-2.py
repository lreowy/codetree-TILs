s = input().split()
b = int(s[0])
a = int(s[1])


while b>=a:
    if b % 2 ==0:
        print(b, end=" ")
    b -= 1
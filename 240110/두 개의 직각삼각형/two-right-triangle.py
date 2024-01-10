n = int(input())
for i in range(n,0,-1):
    if n == i:
        print(n*"*",end="")
        print(n*"*")
    if n != i:
        print(i*"*",end="")
        print((n-i)*" ",end="")
        print((n-i)*" ",end="")
        print(i*"*")
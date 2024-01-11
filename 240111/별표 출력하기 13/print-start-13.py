n = int(input())
plus = 1
minus = n
if n == 1:
    print("*")
    print("*")
else:
    for i in range(n):
        if i%2==0:
            print("* "*minus)
            minus -= 1
        else:
            print("* "*plus)
            plus += 1
    if n%2 == 0:
        minus = int(n/2)
        plus = minus+1
        for k in range(n):
            if k%2==0:
                print("* "*minus)
                minus -= 1
            else:
                print("* "*plus)
                plus += 1
    else:
        plus = int(n/2)+1
        minus = n-plus
        for j in range(1,n+1):
            if j%2==0:
                print("* "*minus)
                minus -= 1
            else:
                print("* "*plus)
                plus += 1
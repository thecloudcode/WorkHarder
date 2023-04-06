def fib(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
x = list(map(int, input().split()))
z=max(x)
l = []
for i in range(z + z):
    l.append(fib(i))
ind=0
for i in x:
    if ind==len(x)-1:
        if i in l:
            print("and "+str(i) + " is valid.")
        else:
            print("and "+str(i) + " is invalid.")
        break
    if i in l:
        print(str(i)+" is valid, ",end="")
    else:
        print(str(i)+" is invalid, ",end="")
    ind+=1
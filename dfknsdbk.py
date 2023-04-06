def fib(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
x = list(map(str, input().split()))
flag=0
for i in x:
    if ord(i[0])<48 or ord(i[0])>57:
        flag=-1
if flag==-1:
    print("Please enter numbers")
else:
    xx=[]
    for i in x:
        xx.append(int(i))
    z=max(xx)
    z=max(4,z)
    l = []
    for i in range(z + z):
        l.append(fib(i))
    ind=0
    for i in xx:
        if len(xx)>1 and ind==len(xx)-1:
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

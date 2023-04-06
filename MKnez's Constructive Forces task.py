for _ in range(int(input())):
    n=int(input())
    a=[]
    if n==3:
        print("NO")
    elif n%2==0:
        print("YES")
        for i in range(n//2):
            a.append("1")
            a.append("-1")
        print(' '.join(a))
    else:
        print("YES")
        x=int(n/2)
        for i in range(int(n/2)):
            a.append(str(int(1-x)))
            a.append(str(int(x)))
        a.append(str(int(1-x)))
        print(' '.join(a))

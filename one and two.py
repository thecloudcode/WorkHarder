for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    p=1
    c=0
    for i in x:
        p*=i
    pp=1
    f=-1
    for i in x:
        pp*=i
        p/=i
        c+=1
        if pp==p:
            f=i
            break
    print(c if f!=-1 else f)

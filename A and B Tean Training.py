n,m=map(int,input().split())
a=n+m
n=max(n,m)
m=a-n
if n>=2*m:
    if n%2==1 and m-(n//2)>=2:
        print(min((n//2)+1,m))
    else:
        print(min(n//2,m))
else:
    c=0
    while(n>1 or m>1):
        while(n>=m):
            n-=2
            m-=1
            # print(c)
            if n<0 or m<0:
                break
            c+=1

        while(m>=n):
            n-=1
            m-=2
            # print(c)
            if n<0 or m<0:
                break
            c+=1

        if n <= 0 or m <= 0:
            break
    print(c)

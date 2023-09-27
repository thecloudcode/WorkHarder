a,b=map(int,input().split())
c,d=map(int,input().split())
first=b
second=d
if b%2==1 and a%2==0 and c%2==0 and d%2==0:
    print(-1)
elif d%2==1 and a%2==0 and b%2==0 and c%2==0:
    print(-1)
else:
    ans=-1
    f=True
    while(1):
        while(first<=second):
            if first==second:
                f=False
                ans=first
                break
            first+=a
        if f==False:
            break
        while(first>second):
            second+=c
    print(ans)
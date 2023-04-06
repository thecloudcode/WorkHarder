n,m=map(int,input().split())
x=list(map(int,input().split()))

last=1
ans=0
for i in x:
    if i>=last:
        ans+=i-last
    else:
        ans+=n-last+i
    last=i
print(ans)
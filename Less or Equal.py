n,k=map(int,input().split())
x=sorted(list(map(int,input().split())))

if k==0:
    ans=x[0]-1
else:
    ans=x[k-1]

c=0
for i in x:
    if i<=ans:
        c+=1
print(-1 if (c!=k or ans<1) else ans)
n=int(input())
x=list(map(int,input().split()))

c=0
ans=0
final=0
for i in x:
    if len(x)==1:
        if x[0]==0:
            final=1
        else:
            final=0
        break
    if x.count(0)==0:
        final=n-1
        break
    if x.count(1)==0:
        final=n
        break
    if i==1:
        c+=1
    if ans==0 and i==1:
        continue
    else:
        if i==1:
            ans-=1
        else:
            ans+=1
            final=max(final,ans)
print(final+c)
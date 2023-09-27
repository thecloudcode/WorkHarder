from collections import defaultdict
d=defaultdict(lambda:0)
n=int(input())
a=list(map(int,input().split()))

for i in a:
    d[i]+=1

x=list(d.values())
s=sum(x)-x[0]
ans=0
for i in x:
    if s-i<=0:
        ans+=s
        break
    ans+=i
    s-=i
print(x,s)
print(ans)


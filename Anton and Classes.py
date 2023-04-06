n=int(input())
b=0
ax,bx=map(int,input().split())
for i in range(n-1):
    a,b=map(int,input().split())
    bx=min(bx,b)
    ax=max(ax,a)
m=int(input())
axx,bxx=map(int,input().split())
for i in range(m-1):
    a,b=map(int,input().split())
    axx=max(axx,a)
    bxx=min(bxx,b)
# print(ax,bx,axx,bxx)
ans=max(axx-bx,ax-bxx)
print(0 if ans<=0 else ans)
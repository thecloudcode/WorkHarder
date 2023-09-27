n,a,b,c,d = map(int,input().split())

ans=0
for i in range(1,n+1):
    maxx=max(a+b+i+1,max(a+c+i+1,max(c+d+i+1,b+d+i+1)))
    e=maxx-(a+b+i)
    f=maxx-(a+c+i)
    g=maxx-(c+d+i)
    h=maxx-(b+d+i)
    x=max(e,max(f,max(g,h)))
    ans+=n+1-x
print(ans if ans>=0 else 0)

def dist(a,b,c,d):
    return (((a-c)**2)+((b-d)**2))**0.5

n,vb,vs=map(int,input().split())
x=list(map(int,input().split()))[1::]
xx,yy=map(int,input().split())
mintime=-1
lol=0
for i in range(n-1):
    time=(x[i]/vb)+dist(x[i],0,xx,yy)/vs
    if mintime==-1:
        mintime=time
    elif time<mintime:
        mintime=time
        lol=i
    elif time==mintime:
        if dist(x[lol],0,xx,yy)>dist(x[i],0,xx,yy):
            lol=i
print(lol+2)
a,b,c=map(int,input().split())

m=min(a//3,min(b//2,c//2))
ans=m*7

a= 3 if a%3==0 else a%3
b=2 if a%2==0 else a%2
c=2 if c%2==0 else c%2

i=0
x=[1,1,2,3,1,3,2,1,1,2,3,1,3,2]

i=0
ii=0
cmax = 0

for _ in range(14):
    i=[ii].copy()[0]
    aa = [a].copy()[0]
    bb = [b].copy()[0]
    cc = [c].copy()[0]
    cget = 0
    while(i<14):
        if x[i]==1 and aa<=0 or x[i]==2 and bb<=0 or x[i]==3 and cc<=0:
            cmax=max(cmax,cget)
            break
        if x[i]==1 and aa>0:
            aa-=1
            cget+=1
        if x[i]==2 and bb>0:
            bb-=1
            cget+=1
        if x[i]==3 and cc>0:
            cc-=1
            cget+=1
        i+=1
    ii+=1
print(ans,cmax)

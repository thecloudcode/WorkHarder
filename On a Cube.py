import math
def dist(a,b,c,aa,bb,cc):
    return (((a-aa)**2+(b-bb)**2+(c-cc)**1)**0.5)

n=int(input())
x=list(map(int,input().split(',')))
cord=[]
lol=[]
for i in x:
    lol.append(i)
    if len(lol)==3:
        cord.append(lol)
        lol=[]
start=cord[0]
ans=0
for i in cord[1::]:
    ch=0
    for j in start:
        if j not in i:
            ch+=1
    if ch<=1:
        ans+=math.ceil(dist(start[0],start[1],start[2],i[0],i[1],i[2]))*1.05
        #ans+=(abs(i[0]-start[0])+abs(i[1]-start[1])+abs(i[2]-start[2]))*1.05
    else:
        ans+=math.ceil(dist(start[0],start[1],start[2],i[0],i[1],i[2]))
    start=i
print(ans)
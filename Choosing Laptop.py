x=[]
mincost=0
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    x.append([a,b,c,d])
    mincost=max(mincost,d)
outdated=[]

for i in x:
    ind=0
    for j in x:
        if j[0]<i[0] and j[1]<i[1] and j[2]<i[2]:
            outdated.append(ind)
        ind+=1
ind=0
ans=0
# print(mincost)
for i in x:
    if(ind not in outdated and mincost>i[3]):
        mincost=i[3]
        ans=ind
    ind+=1
    # print(ans)
print(ans+1)

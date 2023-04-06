from collections import defaultdict
n=int(input())
x=list(map(int,input().split()))

dif=defaultdict(lambda:-1)
ind=defaultdict(lambda:-1)

c=0
for i in range(n):
    if ind[x[i]]==-1:
        ind[x[i]]=i
        c+=1
    else:
        if dif[x[i]]==-1:
            dif[x[i]]=i-ind[x[i]]
            ind[x[i]]=i
        elif i-ind[x[i]]==dif[x[i]]:
            dif[x[i]]=i-ind[x[i]]
            ind[x[i]]=i
    # print(dif,ind)
print(c)
lol=[]
for i in range(n):
    if x[i] not in lol:
        if dif[x[i]]==-1:
            print(x[i],0)
        else:
            print(x[i],dif[x[i]])
        lol.append(x[i])

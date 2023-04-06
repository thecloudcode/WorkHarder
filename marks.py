from collections import defaultdict
n,m=map(int,input().split())
x=[]
for i in range(n):
    x.append(list(input()))
c=0
d=defaultdict(lambda:-1)
for i in range(m):
    maxx=-1
    ind=[]
    for j in range(n):
        if int(x[j][i])>maxx:
            maxx=int(x[j][i])
            ind=[j]
        elif int(x[j][i])==maxx:
            ind.append(j)
    for ii in ind:
        if d[ii]!=-1:
            d[ii]=maxx
            c+=1
print(c)
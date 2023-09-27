# from collections import defaultdict
# d1=defaultdict(lambda: 0)
# d2=defaultdict(lambda: 0)

n,m=map(int,input().split())

x=list(map(int,input().split()))[::-1]
# x.sort(reverse=True)
y=list(map(int,input().split()))[::-1]
# y.sort(reverse=True)

c=0
e=0
ind1=0
ind2=0
lx=len(x)
ly=len(y)
while(ind1<lx and ind2<ly):
    if x[ind1]==y[ind2]:
        ind1+=1
        ind2+=1
    elif x[ind1]!=y[ind2] and y[ind2]>x[ind1]:
        e+=1
        ind2+=1
    elif x[ind1]!=y[ind2] and y[ind2]<x[ind1]:
        if e>0:
            e-=1
        else:
            c+=1
        ind1+=1
if ind1<lx:
    c+=lx-ind1
    if e>=c:
        c=0
    else:
        c-=e
    # if e>=lx-ind1:
    #     c+=0
    # else:
    #     c+=lx-ind1-e
    #
print(c)


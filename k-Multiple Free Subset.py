from collections import defaultdict
d=defaultdict(lambda: 0)
# dd=defaultdict(lambda: 0)

n,k=map(int,input().split())
x=sorted(list(map(int,input().split())))
c=0
f=True

for i in range(n):
    if k==1:
        # print(n)
        f=False
        break
    if d[x[i]]==2:
        continue
    if d[x[i]]==0:
        d[x[i]*k]=2
    if d[x[i]]==0:
        c+=1
        d[x[i]]=1


print(c if f else n)
# print(dict(d))
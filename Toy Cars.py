from collections import defaultdict
d=defaultdict(lambda:0)

n=int(input())
x=[]
for i in range(n):
    x.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if x[i][j]==1:
            d[i]+=1
        if x[i][j]==2:
            d[j]+=1
        if x[i][j]==3:
            d[i]+=1
            d[j]+=1

ans=[]
for i in range(n):
    if d[i]==0:
        ans.append(str(i+1))
print(len(ans))
print(' '.join(ans))
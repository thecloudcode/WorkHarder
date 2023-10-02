from collections import defaultdict
d=defaultdict(lambda:0)
c=0
xx=[]
n,m=map(int,input().split())

for i in range(n):
    x=list(map(int,input().split()))
    xx.append(x)
    for i in x[1::]:
        d[i]+=1

for i in xx:
    flag = True
    for j in i[1::]:
        if d[j]>1:
            print(i,j)
            flag=False
            break
    if flag:
        print(i,"got for this")
        c+=1
print(c)


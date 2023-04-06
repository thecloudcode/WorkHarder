n=int(input())
x=list(map(int,input().split()))
if 1 in x:
    flag=True
else:
    flag=False
xx=[]
c=0
# flag=
if flag:
    for i in x[x.index(1)+1::]:
        if i==0:
            c+=1
        else:
            c+=1
            xx.append(c)
            c=0
    p=1
    for i in xx:
        p*=i
    print(p)
else:
    print(0)

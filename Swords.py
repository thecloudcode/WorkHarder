from collections import defaultdict
d=defaultdict(lambda:0)
a,b=map(int,input().split())
x=list(map(int,input().split()))
for i in x:
    d[i]+=1
for i in range(b):
    z,zz=map(int,input().split())
    cal=(zz-z+1)//2
    if (zz-z+1)%2==0 and cal<=d[-1] and cal<=d[1]:
        print(1)
    else:
        print(0)
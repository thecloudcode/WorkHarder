# from collections import defaultdict
for _ in range(int(input())):
    # d=defaultdict(lambda:0)
    mone=0
    mtwo=0
    m,n=map(int,input().split())
    x=sorted(list(map(int,input().split())))
    left=-1
    leftflag=True
    right=n-1
    for i in range(n):
        if x[i]>0 and leftflag:
            left=i
            leftflag=False
        if x[i]==-1:
            mone+=1
        if x[i]==-2:
            mtwo+=1





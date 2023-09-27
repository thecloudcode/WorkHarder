from collections import defaultdict
for _ in range(int(input())):
    d=defaultdict(lambda:0)
    dd=defaultdict(lambda:0)
    n=int(input())
    c=0
    for __ in range(n):
        x=list(map(int,input().split()))
        for i in x[1::]:
            if d[i]==0:
                d[i]=1
                dd[__+1]=1
                c+=1
                break
    i1=1
    i2=1
    if c==n:
        print("OPTIMAL")
    else:
        flag=True
        print("IMPROVE")
        while(i1<=n):
            if dd[i1]==0:
                while(i2<=n):
                    if d[i2]==0:
                        print(i1,i2)
                        flag=False

                        break
                    i2+=1
            i1+=1
            if flag==False:
                break


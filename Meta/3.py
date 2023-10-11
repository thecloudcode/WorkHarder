import math
from collections import defaultdict
d=defaultdict(lambda: [])

for _ in range(int(input())):
    xxx=[]
    n=int(input())
    x=[i for i in range(101)]
    maxl=len(x)
    # x=list(map(int,input().split()))
    # a,b,c=map(int,input().split())
    flag=True
    ans=False
    ii=0
    while(1):
        xx=[]
        s = 41
        i=41-ii
        ii+=1
        # print(i)
        if i<0:
            break
        nn=n
        while(i>1):
            if nn%i==0 and s-i>=0:
                print(i)
                while(nn%i==0):
                    xx.append(i)
                    nn = nn // i
                    s-=i

                if s<0:
                    xx=[]
                    break
                if s==0 and nn!=1:
                    xx=[]
                    break
                if nn==1:
                    xxx.append(xx)
                    ans=True
                    l=len(xx)
                    ss=sum(xx)
                    if 41-ss+l<maxl:
                        x=xx
                        maxl=41-ss+l
                    xx=[]
                    break
                    # print(f"Case #{_+1}: {l+41-ss}",end=" ")
                    # for i in range(41-ss):
                    #     print("1",end=" ")
                    # for i in range(l):
                    #     if i==l-1:
                    #         print(xx[i])
                    #     else:
                    #         print(xx[i],end=" ")
                    # flag=False
                    # break
            i-=1
    # print(maxl,x)
    print(xxx)
    if ans==False:
        print(f"Case #{_ + 1}: -1")
    # print(x)
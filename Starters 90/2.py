from collections import defaultdict
import math

for _ in range(int(input())):
    n=int(input())
    # x=list(map(int,input().split()))
    # a,b=map(int,input().split())
    s=list(input())
    d=defaultdict(lambda:0)

    for i in s:
        d[i]+=1

    flag=False
    ans=0
    if n%2==0:
        for i in list(d.values()):
            if i%2==1:
                flag=True
                break
        if flag==False:
            ans=1
    else:
        one=0
        if len(set(s))==1:
            ans=2
        else:
            odd=0
            for i in list(d.values()):
                if i%2==1:
                    odd+=1
                    if(odd==2):
                        flag=True
                        break
            if flag==False:
                ans=1
    print(ans)


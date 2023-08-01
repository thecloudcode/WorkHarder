from collections import  defaultdict
import math

for _ in range(int(input())):
    n=int(input())
    x=input()
    # a,b=map(int,input().split())
    # s=input()
    # d=defaultdict(lambda:0)

    ans=0
    a=0
    flaga=True
    b=0
    flagb=False
    for i in range(len(x)):
        if x[i]=='A' and flaga==True:
            a+=1
        elif x[i]=='A' and flaga==False:
            flaga=True
            flagb=False
        elif x[i]=='B' and flagb==True:
            b+=1
        elif x[i]=='B' and flagb==False:
            flagb=True
            flaga=False
    print(a,b)

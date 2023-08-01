from collections import  defaultdict
import math

for _ in range(int(input())):
    n=int(input())
    # nn=int(input())
    # x=list(map(int,input().split()))
    # a,b=map(int,input().split())
    # s=input()
    # d=defaultdict(lambda:0)
    if n==1:
        print(-1)
    elif n%2==1:
        print(-1)
    else:
        x=[str(i) for i in range(1,n+1)]
        print(' '.join(x[::-1]))
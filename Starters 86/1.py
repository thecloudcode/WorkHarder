import math
from collections import defaultdict

for _ in range(int(input())):
    # d = defaultdict(lambda:0)
    # a = map(int, input().split())
    n = int(input())
    # a = int(input())


    x = list(map(int,input().split()))
    xx=[]
    for i in range(n):
        if(i==0):
            xx.append(abs(x[0]-x[1]))
        elif i==n-1:
            xx.append(abs(x[n-1]-x[-2]))
        else:
            xx.append(max(abs(x[i]-x[i+1]),abs(x[i]-x[i-1])))
    print(min(xx))
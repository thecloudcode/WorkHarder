import math
from collections import defaultdict

for _ in range(int(input())):
    # d = defaultdict(lambda:0)
    # a, b = map(int, input().split())
    n = int(input())
    # a = int(input())

    x = list(map(int,input().split()))
    xx=[0]
    for i in range(n-1):
        xx.append(x[i]-x[i+1])
    print(xx)

    for i in range(n-1):
        xx[i+1]+=xx[i]
    # print(xx)
    c=0
    for i in range(n):
        for j in range(i+1,n):
            xxx=x[j]-x[i]
            # print(xxx,xx[j],xx[i])
            if xx[j]-xx[i]!=xxx:
                c+=1
    print(xx)
    print(c)
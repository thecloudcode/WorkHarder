import math
from collections import defaultdict
d=defaultdict(lambda: 0)

for _ in range(int(input())):
    n=int(input())
    # x=list(map(int,input().split()))
    # a,b,c=map(int,input().split())
    if n==1:
        for i in range(40):
            print(1, end=" ")
        print(1)
    else:
        x=[]
        f=2
        while(n>1):
            print(n)
            if n%f==0:
                x.append(f)
                n=n//f
            else:
                f+=1
        print(n)
        # print(n)
        z=sum(x)
        l=len(x)

        if z==41 and n==1:
            print(f"Case {_+1}:",l, end=" ")
            for i in range(l):
                if i==l-1:
                    print(x[i])
                else:
                    print(x[i],end=" ")
        elif z<41:
            # print(x)
            print(f"Case {_+1}:",l, end=" ")
            for i in range(41-z):
                print(1, end=" ")
            for i in range(l):
                if i == len(x) - 1:
                    print(x[i])
                else:
                    print(x[i], end=" ")
        else:
            print(f"Case {_+1}:",0, end=" ")
            print(x)
            print(-1)


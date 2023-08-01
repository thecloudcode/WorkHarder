import math
from collections import defaultdict

for _ in range(int(input())):
    # d = defaultdict(lambda:0)
    # a = map(int, input().split())
    n,mm = map(int,input().split())
    x=list(map(int,input().split()))
    # print(len(set(x)))
    m=min(x)
    c=0
    flag=True

    if m<=mm:
        if(len(set(x))==1):
            print(0)
        else:
            for i in x:
                if i!=m:
                    if(math.gcd(i,m))!=m:
                        flag=False
                        break
                else:
                    c+=1
            if flag:
                print(1)
                print(m)
            else:
                
    else:
        print(1)
        print(1)
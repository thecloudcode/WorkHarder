import math
from collections import defaultdict

for _ in range(int(input())):
    # d = defaultdict(lambda:0)
    # a = map(int, input().split())
    n = int(input())
    # a = int(input())


    s = list(input())
    if n<2:
        print("Ramos")
    else:
        slow=0
        fast=1
        c=0
        while(fast<n and slow<n-1):
            print(slow,fast,c)

            if(s[slow]==s[fast]):
                fast+=1
            else:
                s[slow]=''
                s[fast]=''
                while(s[slow]=='' and slow<n-1):
                    slow+=1
                while(fast<n and (s[fast]=='' or fast==slow) ):
                    fast+=1
                    if(fast==n-1):
                        break
                c+=1
        print("Ramos" if c%2==0 else "Zlatan")

import math
from collections import defaultdict
d=defaultdict(lambda: 0)

for _ in range(int(input())):
    n=int(input())
    # x=list(map(int,input().split()))
    # a,b,c=map(int,input().split())

    x=[]
    while(n>1):
        s=41
        for i in range(0,39):
            if n%(s-i)==0:
                if s - i <= 0 or n <= 1:
                    continue  # Avoid division by zero and infinite loop
                # z=int(math.log(n,s-i))
                # print(z,s-i)
                x.append(s-i)
                s-=(s-i)
                n//=(s-i)
    print(x)

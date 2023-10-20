# from collections import defaultdict
# d=defaultdict(lambda:0)
import math

for _ in range(int(input())):
    # n=int(input())
    # x=list(map(int,input().split()))
    a,b,c=map(int,input().split())

    if a%b==0 or b%a==0:
        print(min(a,b)*2)
    elif a==b:
        print(a*2)
    else:
        x=math.gcd(a,b)
        if c==1:
            print(min(a,b)+x)
        else:
            print(x*2)
        # if c==1:
        #     if min(a,b)==1:
        #         print(2)
        #     else:
        #         print(min(a,b)+1)
        # else:
        #     print(2)




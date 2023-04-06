import math
from collections import defaultdict
#
for _ in range(int(input())):
    # d=defaultdict(lambda:0)
    # a, b = map(int, input().split())
    n = int(input())
    x=1
    c = 40
    ans = ""
    if n%2==0:
        print(-1)
    if n==1:
        print(0)
    else:
        while(n!=1 and c>0):
            if((n+1)//2)%2==1:
                n=(n+1)//2
                ans+="1 "
            else:
                n=(n-1)//2
                ans+="2 "
        if c<0:
            print(-1)
        elif n==1:
            print(len(ans)//2)
            x=list(ans.split(' '))
            x.sort()
            x=x[::-1]
            print(' '.join(x)+" ")
        else:
            print(-1)
        #     if (2*x)+1==n:
        #         x=(2*x)+1
        #         ans+="2 "
        #         break
        #     elif (2*x)-1==n:
        #         x=2*x-1
        #         ans+="1 "
        #         break
        #     elif (((2*x)+1)*2)+1<=n:
        #         x=(x*2)+1
        #         ans+="2 "
        #     else:
        #         x=(x*2)-1
        #         ans+="1 "
        #     if x==n:
        #         break
        # print(len(ans)//2)
        # print(ans)


    # s = input()
    # x = list(map(int, input().split()))

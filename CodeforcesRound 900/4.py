import math
from collections import defaultdict

# d = defaultdict(lambda: 0)

for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        l, k = map(int, input().split())

        ans=-1
        ansgot=False
        cal=-1
        start=False
        for j in range(l-1,n):
            if start==False:
                cal=x[j]
                start=True
            else:
                cal=cal & x[j]
            if cal>=k:
                # and x[ans]>=x[j]:
                if ansgot==False:
                    ans=j
                    print("got it", ans)
                    ansgot=True
                elif ansgot:
                    if x[ans]>=x[j]:
                        print("got it again", ans)

                        ans=j
            # print("lol",cal,j,ans)
        if ansgot==False:
            print(-1, end=" ")
        else:
            print(ans+1, end=" ")
    print()





import math
from collections import defaultdict
#
for _ in range(int(input())):
    # d=defaultdict(lambda:0)
    # a, b = map(int, input().split())
    n = int(input())
    # s = input()
    x = sorted(list(map(int, input().split())))
    summ=[0,1]
    flag=True
    lol=[0]
    for i in x:
        if i not in summ:
            flag=False
            break
        else:
            summ.remove(1)
            for j in summ:
                lol.append(j+i)

            summ=list(set(lol))
            summ.append(1)
            lol = [0]
        # print(i,summ)
        # print("end")
    print("YES" if flag else "NO")


import math
xx=[]
f=True
for _ in range(int(input())):
    x=int(input())
    if x%2==0:
        xx.append(x//2)
    else:
        if f:
            xx.append(math.ceil(x/2))
            f=not f
        else:
            xx.append(x//2)
            f=not f
for i in xx:
    print(i)

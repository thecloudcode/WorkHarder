import math
for _ in range(int(input())):
    n=int(input())
    x=math.floor(n/2)
    y=n-x
    xx=sum([int(i) for i in list(str(x))])
    yy=sum([int(i) for i in list(str(y))])
    if abs(xx-yy)>1:
        if xx<yy:
            x-=1
        else:
            y-=1
    print(x,y)
import math
a,b=map(int,input().split())
if a<b:
    print(-1)
elif a==b:
    print(a)
else:
    for i in range(math.ceil(a/2),a+1):
        if i%b==0:
            print(i)
            break
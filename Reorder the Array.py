import math
n=int(input())
x=list(map(int,input().split()))
dis=len(set(x))
if dis>=math.ceil(n/2):
    print(math.ceil(n/2))
elif dis==1:
    print(0)
else:
    print(dis-1)

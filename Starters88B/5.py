import math
from collections import defaultdict

for _ in range(int(input())):
    # d = defaultdict(lambda:0)
    a, b, c = map(int, input().split())
    # n = int(input())
    # a = int(input())
    x=str(bin(a))[2::]
    y=str(bin(b))[2::]
    lx=len(x)
    ly=len(y)
    l=max(lx,ly)
    if lx<l:
        x="0"*(l-lx)+x
    if ly<l:
        y="0"*(l-ly)+y
    c=0
    for i,j in zip(x,y):
        if i!=j:
            c+=1
    print(int(math.pow(2,c)))


    # x = list(map(int,input().split()))
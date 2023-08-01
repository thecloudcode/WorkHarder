import numpy as np
n = 3
m = 4
arr = np.zeros((n, m))

for _ in range(int(input())):
    n,m=map(int,input().split())
    a,b=map(int,input().split())
    x,y=map(int,input().split())

    arr[a,b]=1
    arr[x,y]=2

    if abs(a-x)==1 and abs(b-y)==1:
        arr[]


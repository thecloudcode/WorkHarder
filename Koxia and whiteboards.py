import math
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    # b.sort()
    # if n==m:
    #     print(sum(b))
    # elif n<m:
    #     print(sum(b[::-1][:n:]))
    # else:
    #     print(sum(a[::-1][:n-m:])+sum(b))
    for i in b:
        t=False
        for j in range(n):
            if i>a[j]:a[j]=i;t=True;break
        if not t:a[0]=i;a.sort()
        else:t=False;a.sort()
    print(sum(a))

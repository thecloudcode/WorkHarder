import math
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    if b<a:
        print(1)
    else:
        print(math.ceil(n/a))
import math
#
for _ in range(int(input())):
#     a, b = map(int, input().split())
    n = int(input())
#     s = input()
    x = list(map(int, input().split()))
    e=0
    o=0
    for i in x:
        if i%2==0:
            e+=1
        else:
            o+=1
    if e>0 and o%2==0:
        print("YES")
    elif e==0 and o%2==0:
        print("YES")
    else:
        print("NO")
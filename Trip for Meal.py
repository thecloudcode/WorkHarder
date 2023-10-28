n=int(input())-1
a=int(input())
b=int(input())
c=int(input())

from collections import defaultdict
d=defaultdict(lambda : 0)

curr = 1
s=0
for i in range(n):
    if curr == 1:
        if a<b:
            curr = 2
            s+=a
        else:
            curr = 3
            s+=b
    elif curr == 2:
        if a<c:
            curr = 1
            s+=a
        else:
            curr = 3
            s+=c
    elif curr == 3:
        if b<c:
            curr = 1
            s+=b
        else:
            curr = 2
            s+=c
    print(s)
print(s)

from collections import defaultdict
d=defaultdict(lambda: 0)
dd=defaultdict(lambda: 0)
last=200001
for _ in range(int(input())):
    x=input()
    d[last]=x
    last-=1

for i in list(dict(d).values())[::-1]:
    if dd[i]==0:
        print(i)
        dd[i]=1

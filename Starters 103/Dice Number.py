import math
from collections import defaultdict

for _ in range(int(input())):
    x=list(map(int,input().split()))
    a=sorted(x[:3:])
    b=sorted(x[3::])
    aa=""
    bb=""
    for i in a:
        aa=str(i)+aa
    for i in b:
        bb=str(i)+bb
    if int(aa)>int(bb):
        print("Alice")
    elif int(aa)<int(bb):
        print("Bob")
    else:
        print("Tie")
    # print(aa,bb)
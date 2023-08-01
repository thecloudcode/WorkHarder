from collections import defaultdict

for _ in range(int(input())):
    d=defaultdict(lambda:0)

    n=int(input())
    x=list(map(int,input().split()))

    c=0
    for i in x:
        if i==0:
            c+=1
        else:
            d[c]+=1
            c=0
    x=list(d.keys())
    if len(x)==0:
        print("Yes")
    elif len(x)==1:
        print("No")
    else:
        xx=x[-1]
        xxx=x[-2]
        if xx%2==0:
            print("No")
        else:
            if xxx


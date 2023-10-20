from collections import defaultdict

for _ in range(int(input())):
    d = defaultdict(lambda: 0)

    n,k = map(int,input().split())
    x = list(map(int, input().split()))
    # a, b = map(int, input().split())
    c=0
    for i in x:
        d[i]+=1
        c+=1
    z=list(d.keys())
    while(c):
        for i in z:
            if d[i]>0:
                print(i,end=" ")
                d[i]-=1
                c-=1
            if c==0:
                break
    print()


from collections import defaultdict
d=defaultdict(lambda: 0)
d[(0,0)]=1
# c=defaultdict(lambda: 0)

n,q=map(int,input().split())

two=0
for _ in range(q):
    a,b=map(int,input().split())

    if d[(a, b)] == 0:
        d[(a, b)] = 1

    elif d[(a, b)] == 1:
        d[(a, b)] = 0


    if a==1:
        if d[(2,b)]==1 or d[(2,b-1)]==1 or d[(2,b+1)]==1:
            if d[(a,b)]==1:
                two+=1
            else:
                two-=1
    elif a==2:
        if d[(1,b)]==1 or d[(1,b-1)]==1 or d[(1,b+1)]==1:
            if d[(a,b)]==1:
                two+=1
            else:
                two-=1
    print("Yes" if two==0 else "No")

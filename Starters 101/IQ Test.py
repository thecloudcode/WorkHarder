n=int(input())
x=list(map(int,input().split()))
e=0
oi=0
o=0
oe=0
for i in range(n):
    if x[i]%2==0:
        e+=1
        oe=i
    else:
        o+=1
        oi=i
    if e>1 and o==1:
        print(oi+1)
        break
    if e==1 and o>1:
        print(oe+1)
        break

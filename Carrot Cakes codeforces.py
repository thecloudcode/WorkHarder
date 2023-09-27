import math
n,t,k,d=map(int,input().split())
first=math.ceil(n/k)*t
tt=0
while(n>0):
    if tt>=d:
        if (tt-d)%t==0 and (tt-d)!=0:
            n-=k
    if n<=0:
        break
    if tt%t==0 and tt!=0:
        n-=k
    if n<=0:
        break
    tt+=1
# print(first)
# print(tt)
print("YES" if tt<first else "NO")
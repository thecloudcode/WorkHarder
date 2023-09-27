n=int(input())
x=list(map(int,input().split()))
if 1 in x:
    start=x.index(1)
else:
    start=len(x)
# print(start)
ans=0
zero=0
one=0
for i in x[start::]:
    if i==1:
        if ans==0:
            ans=zero+1
        else:
            ans*=(zero+1)
        zero=0
        one+=1
    else:
        zero+=1
if one==1:
    print(1)
elif one==0:
    print(0)
else:
    print(ans)


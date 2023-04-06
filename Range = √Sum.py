import math
for _ in range(int(input())):
    n=int(input())
    a=[]
    i=1
    while(i<=n):
        a.append((2*i)-1)
        i+=1
    x=(n+1)*(n+1)-(n*n)
    print(a)
    if x%2==0:
        a[0]+=x//2
        a[-1]+=x//2
    else:
        a[0]+=x//2)
        a[-1]+=(x//2)
    print(a)

    # x=(2*n)-1
    # a=[1]
    # for i in range(n-1):
    #     a.append(x-(n-2))
    # print(a)
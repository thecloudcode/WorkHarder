for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=a.copy()
    b.sort()
    s=""
    for i,j in zip(a,b):
        if i!=b[-1]:
            s+=" "+str(i-b[-1])
        else:
            s+=" "+str(i-b[-2])
    print(s[1::])

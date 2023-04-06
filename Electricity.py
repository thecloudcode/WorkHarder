for _ in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    X=[]
    Y=[]
    d={}
    for i in range(1,N+1):
        d[i]=0
    for i in range(N-1):
        x,y=map(int,input().split())
        X.append(x)
        Y.append(y)
        d[x]+=1
    XX=A.copy()
    XX.sort()
    m=0
    i=0
    while(i<N):
        if A[i]==max(A):
            if d[A[i]]>m:
                m=d[A[i]]
        i+=1
    # for i in XX[::-1]:
    #     if d[i]>m:
    #         m=d[i]
    print("Case #" + str(_ + 1) + ":", m)

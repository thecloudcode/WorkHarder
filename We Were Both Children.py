from collections import defaultdict
for _ in range(int(input())):
    d=defaultdict(lambda:0)
    n=int(input())
    x=list(map(int,input().split()))
    maxx=0
    ans=0
    for i in range(1,n+1):
        for j in x:
            # if j>i:
            #     break
            if i%j==0:
                d[i]+=1
                if d[i]>maxx:
                    maxx=d[j]
                    ans=j
    # print(maxx, ans)
    # print(dict(d))
    print(maxx)
    # maxx=0
    # ans=0
    # for i in x:
    #     ii=i
    #     while(ii<=n):
    #         d[ii]+=1
    #         if d[ii]>maxx:
    #             maxx=d[ii]
    #             ans=ii
    #         ii+=i
    # # print(dict(d))
    # print(maxx)

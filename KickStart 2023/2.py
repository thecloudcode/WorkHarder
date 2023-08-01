import math
from collections import defaultdict

for _ in range(int(input())):
    # d = defaultdict(lambda:0)
    # a = map(int, input().split())
    m,r,n=map(int,input().split())
    x=list(map(int,input().split()))



    ans=[]
    needed=[]
    for i in x:
        ans.append(i-r)
        ans.append(i+r)
    # print(ans)
    flag=True
    c=1
    if x[0]-r>0 or x[-1]+r<m:
        flag=False
    else:
        i=0
        new=False
        while(i<2*n and ans[i]<0):
            new=True
            i+=2
        if new:
            i-=1
        else:
            i=1
        while(i<2*n-1):
            # print(i)
            if ans[i]<ans[i+1]:
                flag=False
                break
            if ans[i]>=m:
                break
            if ans[i+1]>=m:
                c+=1
                # print(i)
                break
            elif i+3<2*n and (ans[i]>=ans[i+3]):
                check=ans[i]
                while(check>=ans[i+3]):
                    i+=4
                    if i+3>2*n-1:
                        break
            c+=1
            # print(i,0)
            # needed.append(i-1)
            i+=2
        # if flag==False
        #     break
        # cc=0
        # for i in needed:
        #     if i==0:
        #         break
        #     cc+=1
        # c-=cc

    if flag:
        print("Case #" + str(_ + 1) + ": "+str(c))
    else:
        print("Case #" + str(_ + 1) + ": IMPOSSIBLE")


    # n = int(input())
    # a = int(input())
    # ans=""
    # next=x[0]+r
    # prev=x[0]-r
    # if x[0]-r>0 or x[-1]+r<m:
    #     ans="IMPOSSIBlE"
    # else:
    #     for i in x[1:-1:]:
    #         prev=i-r
    #         if prev>next:
    #             ans = "IMPOSSIBlE"
    #             break
    #         next=i+r
    # print("Case #"+str(_+1)+": "+ans)

    # s = list(input())
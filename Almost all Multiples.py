for _ in range(int(input())):
    # print(_,end=" ")
    n,x=map(int,input().split())
    nn=n
    if n%x!=0:
        print(-1)
    else:
        ans=[]
        i=n-1
        while(i>=0):
            if i==n-1:
                ans.append(1)
            elif nn%(i+1)==0:
                ans.append(nn)
                nn=i+1
            elif i==0:
                ans.append(x)
            else:
                ans.append(i+1)
            i-=1
        for i in range(n):
            if i==n-1:
                print(ans[n-i-1])
            else:
                print(ans[n-i-1],end=" ")
        for i in range(n-1):
            if ans[n-i-1]%(i+1)!=0:
                print("False",ans[n-i-1],i+1)
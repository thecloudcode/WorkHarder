for _ in range(int(input())):
    # d = defaultdict(lambda:0)
    # a = map(int, input().split())
    m,r,n=map(int,input().split())
    x=list(map(int,input().split()))
    prev=[]
    next=[]
    needed=[]
    for i in x:
        prev.append(i-r)
        next.append(i+r)
    i=0
    # print(prev)
    # print(next)
    flag=True
    c=1
    if prev[0]>0 or next[-1]<m:
        flag=False
    else:
        while(i<n-2 and prev[i+1]<0):
            i+=1
        # print(prev[i])
        while(i<n):
            if next[i]>=m:
                break
            if i+1<=n-1:
                if next[i]<prev[i+1]:
                    flag=False
                    break
            current=next[i]
            while(i<n-1):
                if current>=prev[i+1]:
                    i+=1
                else:
                    break
            # print(current,prev[i])
            c+=1
    if flag:
        print("Case #" + str(_ + 1) + ": "+str(c))
    else:
        print("Case #" + str(_ + 1) + ": IMPOSSIBLE")
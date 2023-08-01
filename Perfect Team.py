for _ in range(int(input())):
    x=list(map(int,input().split()))

    if x[2]>=min(x[1],x[0]):
        print(min(x[1],x[0]))
    else:
        ans=int((x[0]+x[1]+x[2])/3)
        print(min(ans,min(x[0],x[1])))
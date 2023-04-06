for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x=0
    for i in range(n):
        for j in range(i,n):
            f = True
            for k in range(1,len(a[i:j+1:])+1):
                # print(a[i:j+1:],(a[i:j + 1:])[:k:])
                if sum((a[i:j+1:])[:k:])<0:
                    # print("gotta")
                    f=False
            if f:
                # print("yep")
                # print(a[i:j+1:])
                x+=sum(a[i:j+1:])
    print("Case #"+str(_+1)+":",x)
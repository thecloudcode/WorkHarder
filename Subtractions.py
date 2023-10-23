for _ in range(int(input())):
    a,b=map(int,input().split())

    ans=0
    while(a>0 and b>0):
        # print(a,b)
        if a>b:
            ans+=a//b
            a%=b
        elif b>a:
            ans+=b//a
            b%=a
        else:
            ans+=1
            break
    print(ans)
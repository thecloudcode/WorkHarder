for _ in range(int(input())):
    n,k=map(int,input().split())
    x=input()

    c=0
    s=0
    for i in range(n-4):
        xx=x[i:i+4:]
        s+=int(x[i]+x[i+1])
        if xx=='0101':
            c+=1
    s+=int(x[-4]+x[-3])+int(x[-3]+x[-2])+int(x[-2]+x[-1])
    print(s-min(c,k)*10)

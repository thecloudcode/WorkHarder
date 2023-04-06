for _ in range(int(input())):
    n=int(input())
    x=[]
    xx=[]
    xxx=0
    f=True
    # 1 2 3 4 5 5 6 7 8 9
    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
    s=[str(i) for i in range(1,(n*n)+1)]
    l=s.copy()[::-1]
    for i in range(n):
        for j in range(n):
            if f:
                x.append(s[xxx])
                f=False
            else:
                x.append(l[xxx])
                xxx+=1
                f=True
        xx.append(x)
        x=[]
    for i in xx:
        if xx.index(i)%2==1:
            print(' '.join(i[::-1]))
        else:
            print(' '.join(i))

for _ in range(int(input())):
    x=input()
    k=int(input())
    a=[]
    c=[]
    ind=0
    for i in list(x):
        c.append(i)
        a.append(int(i+'0'*(len(x)-ind-1)))
        ind+=1
    print(a)
    print(c)
    for i in range(k):
        s=a.copy()
        s.sort()
        x=s[-1]
        if len(c)>1:
            if c.index((str(x))[0])==0 and c[1]==0:
                x=s[-2]
        a.remove(x)
        c.remove((str(x))[0])
        print(a)
        print(c)
        # print(a)
    print(''.join(c))
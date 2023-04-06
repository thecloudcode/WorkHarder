for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    f=True
    if len(set(a))==1:
        print("NO")
    else:
        print("YES")
        a.sort()
        x=[]
        s=[]
        for i in a:
            if str(i) not in s:
                s.append(str(i))
            else:
                x.append(str(i))
        # if s[-1]!=x[0]:
        print(' '.join(s[::-1]+x))
        # else:
            # print()
        # a.sort()

        # a=[str(i) for i in a[::-1]]
        # print(' '.join(a))

for _ in range(int(input())):
    n=int(input())
    s=input()

    c=1
    last=s[0]
    cc=1
    for i in s:
        if i==last:
            cc+=1
        else:
            last=i
            c=max(cc,c)
            cc=1
    c=max(c,cc)
    print(c)

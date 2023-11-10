for _ in range(int(input())):
    n=int(input())

    last=0
    maxx=1
    c=1
    for i in range(1,int(n**0.5)+1):
        print(i)
        if
        if n%i==0:
            if last+1==i:
                c+=1
            else:
                maxx=max(maxx,c)
                c=1
            last=i
    print(c)

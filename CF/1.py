for _ in range(int(input())):
    n,m=map(int,input().split())
    s=input()
    ss=input()
    l=len(s)
    c=0
    flag=False
    while(len(s)<=max(3*len(ss),2*l)):
        if ss in s:
            flag=True
            break
        c+=1
        s+=s
    print(c if flag else -1)
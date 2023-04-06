for _ in range(int(input())):
    n=list(input())
    s=""
    # int c=0
    c=0
    for i in range(len(n)):
        if(n[i]!='0'):
            c+=1
            s+=n[i]+("0"*(len(n)-i-1))+" "
    print(c)
    print(s[:-1:])


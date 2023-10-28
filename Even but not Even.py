for _ in range(int(input())):
    n = int(input())
    s=input()

    flag=False
    ind=0
    c=0
    for i in range(n):
        if int(s[i])%2==1:
            c+=1
            if c==2:
                flag = True
                ind = i
                break
    if flag:
        for i in range(n):
            if i==ind:
                print(s[i])
                break
            else:
                print(s[i],end="")
    else:
        print(-1)
for _ in range(int(input())):
    n=int(input())
    s=list(input())
    k=0
    flag=0
    a=[]
    x=0
    xx=0
    for i in range(1,n+1):
        if x==1:
            a.append(xx+2)
            xx+=2
            x=0
        else:
            a.append(xx+1)
            xx+=1
            x=1
    # print(a)
    i=0
    while(i<n):
        if i==n-1:
            break
        if k==1:
            if s[i]!=s[i+1]:
                flag=-1
                break
            i+=2
            k=0
        else:
            k=1
            i+=1
    if flag==0 and len(s) in a:
        print("YES")
    else:
        print("NO")

    # ss=set(s)
    # print(ss)
    # i=0
    # f=0
    # flag=0
    # while(i<len(s)-1):
    #     if (f)%2==1:
    #         if s[i]!=s[i+1]:
    #             flag=-1
    #             break
    #         else:
    #             i+=2
    #             f+=1
    #             continue
    #     print(s[f],s[i],s[i+1])
    #     i+=1
    #     f+=1
    # if flag==-1:
    #     print("NO")
    # else:
    #     print("YES")
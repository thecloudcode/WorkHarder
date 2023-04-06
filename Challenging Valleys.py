for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x=min(a)
    b=[]
    ind=0
    for i in a:
        if i==x:
            b.append(ind)
        ind+=1
    # print(x,b)
    i=0
    flag=0
    while(i<len(b)-1):
        if b[i+1]-b[i]>1:
            flag=-1
            break
        i+=1

    if flag==0:
        print("YES")
    else:
        print("NO")

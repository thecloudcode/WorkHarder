for _ in range(int(input())):
    n,m=map(int,input().split())
    flag=False
    x=[]
    for i in range(n):
        s=input()
        x.append(s)
        for i in list(s):
            if i=='^':
                flag=True

    if n==1 or m==1:
        if flag==False:
            print(f"Case {_+1}: 'Possible'")
            for i in x:
                print(i)
        else:
            print(f"Case {_+1}: 'Impossible'")
    else:
        

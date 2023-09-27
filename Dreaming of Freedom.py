for _ in range(int(input())):
    n,m=map(int,input().split())

    if n==1 or m==1:
        print("YES")
    elif n<=m:
        print("NO")
    else:
        if n%m==0:
            print("NO")
        else:
            flag=True
            while(1):
                m=n%m
                print(m)
                if m==0:
                    flag=False
                    break
                elif m==1:
                    flag=True
                    break

            print("NO" if flag==False else "YES")

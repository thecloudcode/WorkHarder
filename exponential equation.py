for _ in range(int(input())):
    n=int(input())
    flag=0
    if n%2==0:
        flag=-1
        print(1,int(n/2))
    else:
        print(-1)
    #     for i in range(1,n+1):
    #         for j in range(1,n+1):
    #             if((i**j)*j+(j**i)*i==n):
    #                 flag=-1
    #                 print(i,int(j))
    # if flag==0:
    #     print(-1)
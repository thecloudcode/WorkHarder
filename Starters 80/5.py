for _ in range(int(input())):
    n=int(input())
    if(n%2==1):
        print(-1)
    else:
        x=['1','2']
        i=3
        while(i<=n):
            x.append(str(i+1))
            x.append(str(i))
            i+=2
        print(' '.join(x))
            # print(i+1,end=" ")
            # print(i,end=" ")

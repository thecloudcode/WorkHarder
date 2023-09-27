for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x=int(input())
    p=0
    for i in range(n):
        j=0
        while(j<n):
            if i<j and a[i]==a[j] and ((i+1)*(j+1))%x==0:
                p+=1
                # print(i,j)
            j=j+x-1

    print(p)

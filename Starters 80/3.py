for _ in range(int(input())):
    # a,b=map(int,input().split())
    n=int(input())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    c=0
    for i,j in zip(x,y):

        if(abs(i-j)<=200):
            c+=1
    print(c)

for i in range(int(input())):
    x,y=map(int,input().split())
    if x<y:
        print(y-x)
    elif x==y:
        print(0)
    elif x>y:
        if(x-y)%2==0:
            print((x-y)//2)
        else:
            print(((x-y)//2)+2)
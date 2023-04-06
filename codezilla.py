for _ in range(int(input())):
    a,b=map(int,input().split())
    if(b>(a+1)):
        print(-1)
    elif(b<-(a-1)):
        print(-1)
    else:
        if(b==a+1):
            print("+"*a)
        elif(b>=1):
            print((((a+1)-b)*"*")+("+"*(b-1)))
        elif(b<=0):
            print(("*"*((a-1)+b))+("-"*(1-b)))

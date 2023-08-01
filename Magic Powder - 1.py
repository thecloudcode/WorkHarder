n,k=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))

c=0
flag=False
while(1):
    for i in range(n):
        y[i]-=x[i]
        if y[i]<0 and k<abs(y[i]):
            flag=True
            break
        elif y[i]<0:
            if k>=abs(y[i]):
                k+=y[i]
                y[i]=0
            else:
                k=0

    # print(y)

    if flag:
        break
    # if k==0:
    #     break
    c+=1
print(c)
x=int(input())%6
n=int(input())%6

if x==2 and n==1:
    print(2)
else:
    n+=6
    n-=x

    if n%6==0 or n%6==5:
        print(0)
    elif n%6==1 or n%6==4:
        print(1)
    elif n%6==2 or n%6==3:
        print(2)
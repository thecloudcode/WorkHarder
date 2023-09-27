a,b=map(int,input().split())
c=0
while(1):
    if a==0 or b==0:
        break
    else:
        if a>=b:
            c+=a//b
            a=a%b
        else:
            c+=b//a
            b=b%a
        # print(a,b)
print(c)
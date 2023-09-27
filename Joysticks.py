a,b=map(int,input().split())
c=0
while(1):
    if a<=0 or b<=0:
        break
    if (a == 1 and b == 1) or (a==0 and b==1) or (a==1 and b==0):
        break
    if a<=b:
        a+=1
        b-=2
        c+=1
    else:
        b+=1
        a-=2
        c+=1
    # print(a,b)
print(c)
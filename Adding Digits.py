a,b,n=map(int,input().split())
aa=a
flag=False
for _ in range(n):
    for i in range(a*10,a*10+10):
        if i%b==0:
            a=i
            flag=True
            break
    if flag==True:
        # a=a*(10**(len(str(aa))+n)-len(str(a)))
        break
print(str(a)+"0"*(len(str(aa))+n-len(str(a))) if flag else -1)
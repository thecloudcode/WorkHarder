n=input()
s=input()

a=0
b=0
curr=0
c=0
for i in s:
    if i=='U':
        b+=1
    if i=='R':
        a+=1
    if curr==0:
        if a>b:
            curr=2
        if a<b:
            curr=1
    if a>b and curr==1:
        curr=2
        c+=1
    if a<b and curr==2:
        curr=1
        c+=1
    # print((a,b))
print(c)
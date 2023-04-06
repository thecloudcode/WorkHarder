s=list(input())
x=-1
for i in s:
    if i=='h':
        x=0
    elif i=='e' and x==0:
        x+=1
    elif i=='l' and x<=2:
        x+=1
    elif i=='o' and x==3:
        x+=1
if x==4:
    print("YES")
else:
    print("-1")
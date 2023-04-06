x=0
cur=0
for i in range(int(input())):
    j=int(input())
    if x==0:
        x+=j+1
        cur=j
    else:
        if cur<=j:
            x+=1+(j-cur)+1
            cur=j
        else:
            x+=cur-j+2
            cur=j
print(x)
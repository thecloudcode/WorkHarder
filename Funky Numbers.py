n=int(input())
flag = False

for i in range(1,n+1):
    need=n-i*(i+1)//2
    if need>=0:
        sq=int((2*need)**0.5)
        if sq*(sq+1)==2*need or sq*(sq-1)==2*need or (sq+1)*(sq+2)==2*need or (sq-2)*(sq-1)==2*need:
            flag=True
            break
print("YES" if flag else "NO")
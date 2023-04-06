x=list(input())
flag=False

c=1
for i in range(len(x)-1):
    if x[i]==x[i+1]:
        c+=1
    else:
        c=1
    if c==7:
        flag=True
        break
print("YES" if flag else "NO")
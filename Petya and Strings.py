x=list(input().lower())
y=list(input().lower())
f=0
for i,j in zip(x,y):
    if ord(i)>ord(j):
        f=1
        break
    elif ord(i)<ord(j):
        f=-1
        break
print(f)
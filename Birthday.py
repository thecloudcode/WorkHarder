n=int(input())
x=sorted(list(map(int,input().split())))

a=[]
b=[]
for i in range(n):
    if i%2==0:
        a.append(str(x[i]))
    else:
        b.append(str(x[i]))
print(' '.join(a)+' '+' '.join(b[::-1]))


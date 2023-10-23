n=int(input())
x=sorted(list(map(int,input().split())))
for i in range(n):
    if i==n-1:
        print(x[i])
    else:
        print(x[i],end=" ")
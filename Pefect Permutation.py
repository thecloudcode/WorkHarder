n=int(input())
if n%2==1:
    print(-1)
else:
    x=[i+1 for i in range(n)]
    i=0
    while(i<n):
        temp=str(x[i])
        x[i]=str(x[i+1])
        x[i+1]=temp
        i+=2
    print(' '.join(x))
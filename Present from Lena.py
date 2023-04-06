n=int(input())
for i in range(n+1):
    print(2*(n-i)*" ",end="")
    x=[str(i) for i in range(i+1)]
    if len(x)==1:
        print(' '.join(x))
    else:
        print(' '.join(x)+" "+' '.join(x[::-1][1::]))
i=n-1
while(i>=0):
    print(2 * (n - i) * " ", end="")
    x = [str(i) for i in range(i + 1)]
    if len(x)==1:
        print(' '.join(x))
    else:
        print(' '.join(x) + " " + ' '.join(x[::-1][1::]))
    i-=1

    
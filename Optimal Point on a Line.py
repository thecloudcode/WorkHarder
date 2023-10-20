n=int(input())
x=sorted(list(map(int,input().split())))

if n%2==1:
    print(x[n//2])
else:
    a=x[n//2]
    b=x[(n//2)-1]
    aa=0
    bb=0
    for i in range((n//2)-1):
        aa+=a-x[i]
    for i in range((n//2)+1):
        aa+=x[i]-a

    for i in range((n//2)-2):
        bb+=b-x[i]
    for i in range(n//2):
        bb+=x[i]-b

    if aa<=bb:
        print(a)
    else:
        print(b)


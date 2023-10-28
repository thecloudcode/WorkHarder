# n=int(input())
for _ in range(int(input())):
    a,b=map(int,input().split())

    s=0
    for i in range(a,b+1):
        if i%2==1:
            s-=i
        else:
            s+=i
    print(s)
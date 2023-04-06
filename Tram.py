x=[]
maxx=0
s=0
for _ in range(int(input())):
    a,b=map(int,input().split())
    s=s-a
    s=s+b
    if s>maxx:
        maxx=s
print(maxx)
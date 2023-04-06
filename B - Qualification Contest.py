a,b=map(int,input().split())
x=[]
for _ in range(a):
    x.append(input())
x=x[:b:]
x.sort()
# x=x[::-1]
for i in range(b):
    print(x[i])
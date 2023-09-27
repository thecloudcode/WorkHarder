n=int(input())
s=list(input())
s*=n
x=[0 for i in range(len(s)*n)]
# print(x)
l=len(s)
for _ in range(int(input())):
    a,b=map(str,input().split())
    a = int(a)
    for i in range(l):
        if s[i]==b and x[i]==0:
            a-=1
            if a==0:
                x[i]=-1
                break
    # print(x)

for i in range(l):
    if x[i]==0:
        print(s[i],end="")
#bacbac

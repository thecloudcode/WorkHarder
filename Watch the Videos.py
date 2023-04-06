n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
x=a[0]
t=a[0]
for i in a[1::]:
    if x+i<=m:
        t+=i
    else:
        t+=i+1
# for i in a[1::]:
#     if x+i<m:
#         t+=i-1
#         print(x,t,1)
#     elif x+i==m:
#         t+=i
#     else:
#         t+=i+2
#         print(x,t,2)
    x=i
print(t)
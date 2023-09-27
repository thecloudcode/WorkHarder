ans=0

def cloud(x,i,s,f,n):
    if i==n and s==f:
        return 1
    if i==n:
        return 0

    if x[i]=='+':
        return cloud(x,i+1,s+1,f,n)
    if x[i]=='-':
        return cloud(x,i+1,s-1,f,n)
    else:
        return cloud(x,i+1,s+1,f,n)+cloud(x,i+1,s-1,f,
a=input()
s=0
for i in a:
    if i=='+':
        s+=1
    else:
        s-=1
b=input()
p=1
for i in b:
    if i=='?':
        p*=2
# print(p)
# print(cloud(b,0,0))
print("{:.12f}".format(cloud(b,0,0,s,len(b))/p))

# def cloud(x,i,s,f,n):
#     global ans
#     if s==f and i==n:
#         ans+=1
#         return
#     if i==n:
#         return
#     if x[i]=='+':
#         s+=1
#     elif x[i]=='-':
#         s-=1
#     else:
#         s=cloud(x,i+1,s+1,f,n)
#         cloud(x,i+1,s-1,f,n)
#         return


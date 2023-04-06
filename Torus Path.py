n=int(input())
a=[]
s=0
for i in range(n):
    x=list(map(int, input().split()))
    a.append(x)
    s+=sum(x)
# print(a)
b=[]
for i in range(n):
    b.append((a[i])[n-i-1])
print(s-min(b))
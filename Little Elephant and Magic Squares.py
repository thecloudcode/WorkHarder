a,r1,aa=map(int,input().split())
r2,b,r22=map(int,input().split())
cc,r3,c=map(int,input().split())

b=int((r1+r3)/2)
a=r2+r22+b-r1-aa
c=r2+r22+b-cc-r3

print(a,r1,aa)
print(r2,b,r22)
print(cc,r3,c)
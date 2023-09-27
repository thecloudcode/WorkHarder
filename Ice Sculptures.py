n=int(input())
x=list(map(int,input().split()))

e=0
o=0
s=0
co=0
ce=0
for i in range(n):
    if i%2==0:
        e+=x[i]
        ce+=1
    else:
        o+=x[i]
        co+=1
    s+=x[i]

flag=True
if s>=s-e and s>=s-o:
    print(s)
    flag=False
if co>=3 and flag:
    if o<e:
        print(s-o)
        flag=False
    # if o<0 and o<e:
if ce>=3 and flag:
    if e<o:
        print(s-e)
        flag=False
if flag:
    print(s)

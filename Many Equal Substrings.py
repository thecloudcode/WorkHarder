n,k=map(int,input().split())
s=input()
x=[s].copy()[0]
l=len(s)

if l==1:
    print(s*k)
else:
    start=0
    next=1
    while(next<l):
        if s[start]==s[next]:
            start+=1
            next+=1
        else:
            start=0
            next+=1
    print(s+s[start::]*(k-1))

# ind=0
# start=0
# end=len(s)-1
# xx=""
# i=0
# while(start<end):
#     if s[start]==s[end]:
#         start+=1
#         end-=1
#     else:
#         break
#
# ind=1
# while(1):
#     x+=x[start]
#     xx+=x[start]
#     start+=1
#
#     if x[ind::]==s:
#         break
#     ind+=1
# print(s+xx*(k-1))
# print(xx)
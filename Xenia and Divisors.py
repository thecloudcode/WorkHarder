from collections import defaultdict
n=int(input())
x=sorted(list(map(int,input().split())))
hash=defaultdict(lambda:0)

for i in x:
    hash[i]+=1

if hash[1]==n/3 and hash[2]==n/3-

# ans=[]
# xx=[]
# y=x[0]
# ind=0
# while(1):
#     for i in range(1,len(x)):
#         # print(x[i],y)
#         if x[i]%y==0:
#             yy=x[i]
#             for j in range(i+1,len(x)):
#                 if x[j]%yy==0:
#                     xx.append([str(y),str(yy),str(x[j])])
#                     x.remove(y)
#                     x.remove(yy)
#                     x.remove(x[j])
#                     y=x[0]
#                     break
#     print(ans)
#     if len(x)==0:
#         break
# for i in ans:
#     print(' ',join(i))
from collections import defaultdict
k=int(input())
s=input()
x=list(set(list(s)))
c=0
hash=defaultdict(lambda:0)

for i in s:
    if hash[ord(i)-97]==0:
        c+=1
    hash[ord(i)-97]+=1

z=""
flag=True
for i in list(hash.values()):
    if i%k!=0:
        flag=False
        break

if flag:
    for i in list(hash.keys()):
        z+=chr(i+97)*(hash[i]//k)
    print(z*k)
else:
    print(-1)


# # print(len(s),len(x))
# if len(x)==k:
#     summ=[]
#     for i in x:
#         summ.append(s.count(i))
#     if len(set(summ))==1:
#         print(''.join(x)*(len(s)//len(x)))
#     else:
#         print(-1)
# else:
#     print(-1)
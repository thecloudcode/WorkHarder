x=list(input())
r=x.index('R')%4
g=x.index('G')%4
y=x.index('Y')%4
b=x.index('B')%4
# print(r,g,y,b)
R=0
G=0
Y=0
B=0
for i in range(len(x)):
    if i%4==r and x[i]=='!':
        R+=1
    if i%4==g and x[i]=='!':
        G+=1
    if i%4==y and x[i]=='!':
        Y+=1
    if i%4==b and x[i]=='!':
        B+=1
print(R,B,Y,G)














# x=list(input())
# ans=[0,0,0,0]
# i=0
# while(i<len(x)-3):
#     if '!' in x[i:i+4:]:
#         # z=3-x[i:i+4:][::-1].index('!')
#         if 'R' not in x[i:i+4:]:
#             ans[0]+=1
#             x[i+x[i:i+4:].index('!')]='R'
#         if 'B' not in x[i:i+4:]:
#             ans[1]+=1
#             x[i+x[i:i+4:].index('!')]='B'
#         if 'Y' not in x[i:i+4:]:
#             ans[2]+=1
#             x[i+x[i:i+4:].index('!')]='Y'
#         if 'G' not in x[i:i+4:]:
#             ans[3]+=1
#             x[i+x[i:i+4:].index('!')]='G'
#         # i+=z
#         # print(x[i:i+4:],i)
#     i+=1
#     # print(i)
# print(ans[0],ans[1],ans[2],ans[3])
n,m=map(int,input().split())
x=[]
z=[]
zz=[]
c=0
for _ in range(m):
    a,b=map(str,input().split())
    if a+b in x or b+a in x:
        c+=1
        # print("yes",x)
    else:
        f=True
        xx=x.copy()
        for i in xx:
            if i[-1]==a:
                x.remove(i)
                x.append(i[:-1:]+b)
                f=False
            elif i[0]==a:
                x.remove(i)
                x.append(b+i[1::])
                f=False
            elif i[-1]==b:
                x.remove(i)
                x.append(i[:-1:]+a)
                f=False
            elif i[0]==b:
                x.remove(i)
                x.append(a+i[1::])
                f=False
            # print("for",x)
        if f:
            x.append(a+b)
            # print("hel",x)

print(c)




# from collections import defaultdict
# n,m=map(int,input().split())
# d = defaultdict(lambda: 0)
# for _ in range(m):
#     a,b=map(int,input().split())
#     d[a]+=1
#     d[b]+=1
# # c=0
# # for i in list(d.values()):
# # print(sum(list(d.values())))
# # print()
# xx=len(set(list(d.keys())+list(d.values())))
# if(sum(list(d.values()))<=2*(xx-1)):
#     print(0)
# else:
#     print((sum(list(d.values()))-2*(xx-1))//2)

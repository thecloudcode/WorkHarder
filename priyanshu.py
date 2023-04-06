a=input("data1: ").split(",")
b=input("data2: ").split(",")
# print(a,b)
print("dictionary with key order")
d={}
aa=[]
bb=[]
for i in a:
    aa.append(int(i))
for i in b:
    bb.append(int(i))
aa.sort()
bb.sort()
for i in range(len(a)):
    print(aa[i],bb[i])
print("dictionary with value order")
for i in range(len(a)):
    print(bb[i],aa[i])
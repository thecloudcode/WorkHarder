# a,b=map(int,input().split())
# s=list(set(list(map(int,input().split()))))
# s.sort()
# s=s[:b:]
# # print(s)
# # print(0 if 0 not in s else 1 if 1 not in s else 2 if 2 not in s else 3)
# f=True
# for i in range(b+1):
#     if i not in s:
#         print(i)
#         f=False
#         break
# if(f): print(b+2)

n,k = map(int,input().split())
arr = list(set(list(map(int,input().split()))))
arr.sort()
arr=arr[:k:]
value = 0
k=True
while True:
    if(value not in arr):
        print(value)
        k=False
        break
    else:
        value += 1
if k:
    print(value)
a,b=map(int,input().split())
for i in range(a):
#     if(i%2==0):
#         print("#"*b)
#     if(i%4==1):
#         print("."*(b-1)+"#")
#     if(i%4==3):
#         print("#"+"."*(b-1))
    print("#"*b if i%2==0 else "."*(b-1)+"#" if i%4==1 else "#"+"."*(b-1))
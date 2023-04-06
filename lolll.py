# Your code here
for _ in range(int(input())):
    n,l,s=map(int,input().split())
    x=l*(l+1)/2
    xx=n*(n+1)/2
    xxx=(l-1)*(l/2)
    # print(x,xx)
    # a=[i for i in range(1,n+1)]
    # x=[]
    # f=0
    # flag=False
    # print(sum(a[::-1][:l:])-a[l-1]+a[l])
    # print(sum(a[:l:])-a[0]+a[l])
    if((s-x)%l==0):
        print("YES")
    elif(x-1+l+1<=s<=xx-xxx-1):
        print("YES")
    else:
        print("NO")
    # if(sum(a[-3::1])<=s):
    # if s >= l * (l + 1) / 2 and s <= sum(a[::-1][:l:]):
    #     for i in range(l,n+1):
    #         # print(f,i)
    #
    #         if(sum(a[f:i:])-min(a[f:i:])+max(a[f:i:])+1>=s>=sum(a[f:i:])-max(a[f:i:])+min(a[f:i:]))-1 and i:
    #             # print(sum(a[f:i:]),i)
    #             flag=True
    #             break
    #         f+=1
    # for i in range(1,n+1):
    #     for j in x:
    #         if j-i==s:
    #             print(j,i)
    #             flag=True
    #             break
    #     if(flag):break
    # print("YES" if flag else "NO")


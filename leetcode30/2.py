nums=[0,8,0,0,0,23]
i=0
l=len(nums)
c=0
while(i<l):
    minn=nums[i]
    xx=nums[i]
    mini=i
    ind=i+1
    while(ind<l):
        xx=xx & nums[ind]
        if minn==0:
            # mini=ind
            break
        if xx<=minn:
            minn=xx
            mini=ind
        if minn==0:
            mini=ind
            break
        ind+=1
    i=mini+1
    # print(nums[:mini])
    # if i==l:
    #     break
    c+=1
    print(minn,i,ind,mini)
    # print(1 & 7)
print(c)
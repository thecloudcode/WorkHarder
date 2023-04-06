import itertools
def findsubsets(S):
    return set(itertools.combinations(S,2))

c=0
nums=[0,1,7,4,4,5]
lower=3
upper=6
print(findsubsets(nums))
for i in findsubsets(nums):
    if i[0]+i[1]>=lower and i[0]+i[1]<=upper:
        print(i)
        c+=1
# for i in range(len(nums)-1):
#     for j in range(i+1,len(nums)):
#         x=nums[i]+nums[j]
#         if(x>=lower and x<=upper):
#             c+=1
print(c)
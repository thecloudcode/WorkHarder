class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # x,y=map(str,input().split())
        ind1=0
        ind2=0
        l=len(str1)
        ll=len(str2)
        while(ind1<l and ind2<ll):
            if ord(str1[ind1])+1==ord(str2[ind2]) or ord(str1[ind1])==ord(str2[ind2]) or (str1[ind1]=='z' and str2[ind2]=='a'):
                ind1+=1
                ind2+=1
            else:
                ind1+=1
        # print(ind1, ind2, l, ll)
        return(ind2==ll)

# Create an instance of the Solution class
solution_instance = Solution()

# Input strings
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Call the method and print the result
result = solution_instance.canMakeSubsequence(str1, str2)
print(result)

# x,y=map(str,input().split())
# ind1=0
# ind2=0
# l=len(x)
# ll=len(y)
# while(ind1<l and ind2<ll):
#     if ord(x[ind1])+1==ord(y[ind2]) or ord(x[ind1])==ord(y[ind2]) or (x[ind1]=='z' and y[ind2]=='a'):
#         ind1+=1
#         ind2+=1
#     else:
#         ind1+=1
# # print(ind1, ind2, l, ll)
# print('true' if ind2==ll else 'false')












# class Solution:
#     def countPairs(self, nums: list[int], target: int) -> int:
#         # x=list(map(int,input().split()))
#         # t=int(input())
#         l=0
#         ll=len(nums)
#         c=0
#         for i in range(l,ll):
#             for j in range(l+1,ll):
#                 # print(x[])
#                 if nums[i]+nums[j]<target:
#                     c+=1
#             l+=1
#         return c
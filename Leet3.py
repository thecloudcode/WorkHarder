import bisect
class Solution:
    def mini(self, nums):
        c = 0
        t = []
        n = len(nums)

        t.append(nums[0])
        for i in range(1, n):
            upperbound = bisect.bisect_right(t, nums[i])

            if upperbound != len(t):
                c += 1
                ind = upperbound
                t[ind] = min(t[ind], nums[i])
            else:
                t.append(nums[i])


        return c

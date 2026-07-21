class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        op=1
        maxi=op
        for i in range(0,len(nums)-1):
            if nums[i]+1==nums[i+1]:
                op=op+1
            elif nums[i]==nums[i+1]:
                continue
            else:
                maxi = max(maxi, op)
                op=1
        maxi = max(maxi, op)
        if len(nums)==0:
            return 0
        else:
            return maxi
        
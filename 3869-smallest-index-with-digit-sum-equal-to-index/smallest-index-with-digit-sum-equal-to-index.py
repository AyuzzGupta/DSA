class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            tot=0
            n=nums[i]
            while n>0:
                rem=n%10
                tot+=rem
                n=n//10
            if tot ==i:
                return i
        return -1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[i]-nums[i-1])!=1:
                return abs(nums[i]-1)
            elif len(nums) not in nums:
                return len(nums)
            elif 0 not in nums:
                return 0

            

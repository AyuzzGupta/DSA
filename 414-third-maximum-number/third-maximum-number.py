class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        l=[]
        for i in range(0,len(nums)):
            if nums[i] not in l:
                l.append(nums[i])
        l.sort(reverse=True)
        if len(l)<3:
            return l[0]
        else:
            return l[2]
        
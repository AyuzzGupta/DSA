class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        cnt =1
        for i in range(0,len(nums)):
            if cnt*k not in nums:
                break
            cnt+=1
            
        return cnt*k
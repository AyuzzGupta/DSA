class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=[]
        cnt=0
        for i in nums:
            if i==1:
                cnt=cnt+1
            else:
                l.append(cnt)
                cnt=0
        l.append(cnt) 
        return max(l)
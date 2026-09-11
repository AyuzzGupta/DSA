class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        n=0
        nd=0
        for i in nums:
            n=n+i
            while i>0:
                rem=i%10
                nd=nd+rem
                i=i//10
        return abs(n-nd)
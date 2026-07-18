class Solution:
    def findGCD(self, nums: List[int]) -> int:
        gcd=0
        max=0
        min=nums[0]
        for i in nums:
            if i>max:
                max=i
        for i in nums:
            if i<min:
                min=i
        for i in range(1,min+1):
            if min%i==0 and max%i==0 and gcd<i:
                gcd=i
        return gcd

        
        
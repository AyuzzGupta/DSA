class Solution:
    def maxProduct(self, n: int) -> int:
        dig=[]
        while n>0:
            rem=n%10
            dig.append(rem)
            n=n//10
        dig.sort()
        return dig[-1]*dig[-2]

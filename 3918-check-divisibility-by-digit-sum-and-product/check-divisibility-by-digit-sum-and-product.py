class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        t=n
        while n>0:
            s=s+(n%10)
            p=p*(n%10)
            n=n//10
        if t%(s+p)==0:
            return True
        else:
            return False
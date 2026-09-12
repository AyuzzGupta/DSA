class Solution:
    def sumOfMultiples(self, n: int) -> int:
        cnt=0
        for i in range(0,n+1):
            if i%3==0:
                cnt=cnt+i
            elif i%5==0:
                cnt=cnt+i
            elif i%7==0:
                cnt=cnt+i
        return cnt

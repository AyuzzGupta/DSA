class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        cntp=1
        cnt=0
        while n>0:
            rem = n%10
            cntp= cntp*rem
            cnt+=rem
            n=n//10
        return cntp-cnt
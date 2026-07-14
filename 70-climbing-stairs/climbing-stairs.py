class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # def fib(n):
        #     if n==0:
        #         return 0
        #     elif n==1:
        #         return 1
        #     else:
        #         return (fib(n-1)+fib(n-2))
        # return fib(n+1)
        a=0
        b=1
        for i in range(0,n):
            c=a+b
            a=b
            b=c
        return c
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        x=num
        n=t
        while t>0:
            x+=1
            t-=1
        t=n
        while t>0:
            x+=1
            t-=1
        return x
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sa=0
        sb=0
        for i in nums:
            if i==i%10:
                sa+=i
            else:
                sb+=i
        if sa>sb or sb>sa:
            return True
        else:
            return False

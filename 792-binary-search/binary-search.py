class Solution:
    def search(self, nums: List[int], target: int) -> int:
        f=0
        for i in nums:
            if i==target:
                return nums.index(i)
                f=1
                break
        if f==0:
            return -1
        
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # prod=1
        # nums.sort(reverse=True)
        # for i in range(0,3):
        #     prod *= nums[i]
        # return prod
        nums.sort()

        p1 = nums[-1] * nums[-2] * nums[-3]   # 3 largest
        p2 = nums[0] * nums[1] * nums[-1]     # 2 smallest + largest

        return max(p1, p2)
        
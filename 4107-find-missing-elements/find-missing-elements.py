class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()

        missing = []
        expected = nums[0]

        for x in nums:
            while expected < x:
                missing.append(expected)
                expected += 1
            if expected == x:
                expected += 1

        while expected <= len(nums):
            missing.append(expected)
            expected += 1

        return missing
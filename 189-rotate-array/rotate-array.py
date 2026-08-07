class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        while k > 0:
            temp = nums.pop()      # last element nikalo
            nums.insert(0, temp)   # beginning mein daalo
            k -= 1

        

        
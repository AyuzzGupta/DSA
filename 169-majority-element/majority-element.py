class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        max_count = d[nums[0]]
        answer = nums[0]

        for key, value in d.items():
            if value > max_count:
                max_count = value
                answer = key

        return answer
            
            
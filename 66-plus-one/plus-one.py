class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in digits:
            num = num * 10 + i
        num = num + 1
        
        li = []
        while num > 0:
            li.append(num % 10)
            num = num // 10
        
        li.reverse()
        return li
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        di=0
        for i in nums:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        for j in d.keys():
            if d[j]>1:
                di=1
        if di>0:
            return True
        else:
            return False
            
        
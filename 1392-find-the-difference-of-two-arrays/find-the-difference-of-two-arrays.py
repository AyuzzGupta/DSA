class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l1=[]
        l2=[]
        answer=[]
        for i in nums1:
            if i not in nums2:
                if i not in l1:
                    l1.append(i)
        for i in nums2:
            if i not in nums1:
                if i not in l2:
                    l2.append(i)
        answer.append(l1)
        answer.append(l2)
        return answer
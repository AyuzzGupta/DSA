class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i=0
        l= len(arr)
        while i<len(arr):
            if arr[i]==0:
                arr.insert(i+1,0)
                i=i+1
            i=i+1
        for j in range (len(arr)-1,l-1,-1):
            arr.pop(j)
        
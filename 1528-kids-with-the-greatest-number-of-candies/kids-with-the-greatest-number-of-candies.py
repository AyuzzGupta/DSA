class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max=candies[0]
        l=[]
        for i in candies:
            if i >max:
                max=i
        for i in candies:
            if i+extraCandies>=max:
                l.append(True)
            else:
                l.append(False)
        return l
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        se=0
        so=0
        for i in range(1,n+1):
            if i%m==0:
                se=se+i
            else:
                so=so+i

        return (so-se)
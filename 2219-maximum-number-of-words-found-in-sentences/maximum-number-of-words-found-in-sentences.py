class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        cnt=0
        maxi=cnt
        for i in sentences:
            for j in i.split():
                cnt=cnt+1
            if cnt>maxi:
                maxi= cnt
                cnt=0
            else:
                cnt=0

        return maxi
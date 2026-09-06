class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d={}
        for i in sentence:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        cnt=0
        for i in d.values():
            cnt+=1
        if cnt==26:
            return True
        else:
            return False
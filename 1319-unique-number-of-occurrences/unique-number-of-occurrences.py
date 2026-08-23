class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        l=[]
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d.values():
            l.append(i)
        for i in range(0,len(l)):
            for j in range(i+1,len(l)):
                if l[i]==l[j]:
                    return False
        return True

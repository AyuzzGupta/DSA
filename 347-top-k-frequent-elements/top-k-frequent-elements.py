class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        ki=0
        l=[]
        for i in nums:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        di = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        for j in di.keys():
            if ki==k:
                break
            l.append(int(j))
            ki=ki+1
        return l

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        di={}
        if len(s)!=len(t):
            return False
        for i in s.lower():
            if i in d.keys():
                d[i]=d[i]+1
            else:
                d[i]=1
        for i in t.lower():
            if i in di.keys():
                di[i]=di[i]+1
            else:
                di[i]=1
        dn = dict(sorted(d.items()))
        din = dict(sorted(di.items()))
        if dn==din:
            return True
        else:
            return False
        

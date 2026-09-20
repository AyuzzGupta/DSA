class Solution:
    def reverseDegree(self, s: str) -> int:
        d={}
        l="abcdefghijklmnopqrstuvwxyz"
        e=0
        a=26
        for i in range(1,27):
            d[l[e]]=a
            e+=1
            a=a-1
        cnt=0
        for i in range(0,len(s)):
            stri =d[s[i]]*(i+1)
            cnt+=stri
        return cnt



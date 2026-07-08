class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sn=s.strip()
        ns=s.split()
        return(len(ns[-1]))
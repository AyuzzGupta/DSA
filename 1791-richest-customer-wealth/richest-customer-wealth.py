class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sumi=0
        for i in range(0,1):
            for j in range(len(accounts[i])):
                sumi =sumi + accounts[i][j]
        n=0

        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                n =n + accounts[i][j]
            if n>sumi:
                sumi=n
                n=0
            else:
                n=0
        return sumi
        

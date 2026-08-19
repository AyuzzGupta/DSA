class Solution:
    def calPoints(self, operations: List[str]) -> int:
        tot=[]
        toti=0
        n="1234567890"
        for i in range(0,len(operations)):
            if operations[i].lstrip("-").isdigit():
                tot.append(int(operations[i]))
            elif operations[i]=="C":
                tot.pop()
            elif operations[i]=="D":
                tot.append(int(tot[-1]*2))
            elif operations[i]=="+":
                tot.append(int(tot[-1]+tot[-2]))
        for i in tot:
            toti=toti+ i
        return toti


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d={
            "U": 1,
            "D":-1
        }
        dh={
            "L":-1,
            "R":1
        }
        t=0
        h=0
        for i in moves:
            if i in d:
                t+=d[i]
            else:
                h+=dh[i]
        if t==0 and h==0:
            return True
        else:
            return False

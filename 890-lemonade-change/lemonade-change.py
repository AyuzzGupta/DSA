class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        Change =[0,0,0]
        for i in bills:
            if i ==5:
                Change[0]=Change[0]+5
            elif i==10:
                if Change[0]>=5:
                    Change[0]-=5
                    Change[1]+=10
                else:
                    return False
            elif i==20:
                # if Change[0]>=15:
                #     Change[0]-=15
                #     Change[2]+=20
                if Change[0]>=5 and Change[1]>=10:
                    Change[0]-=5
                    Change[1]-=10
                    Change[2]+=20
                elif Change[0] >= 15:
                    Change[0] -= 15
                else:
                    return False
        return True

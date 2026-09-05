class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        t=1
        arr=[]
        while len(nums)>0:
            if t%2!=0:
                mina =min(nums)
                nums.remove(mina)
                t=t+1
            else:
                minb=min(nums)
                nums.remove(minb)
                arr.append(minb)
                arr.append(mina)
                t=t+1
        return arr


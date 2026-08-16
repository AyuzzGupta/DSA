class Solution:
    def average(self, salary: List[int]) -> float:
        mini=salary[0]
        maxi=salary[0]
        sumi=0
        for i in salary:
            if i<mini:
                mini=i
            if i>maxi:
                maxi =i
        salary.remove(mini)
        salary.remove(maxi)
        for i in salary:
            sumi+=i
        return sumi/len(salary)
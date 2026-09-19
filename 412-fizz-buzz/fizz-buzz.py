class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        l=[]
        for i in range(0,n):
            ni=i+1
            if ni%3==0 and ni%5==0:
                l.append("FizzBuzz")
            elif ni%3==0:
                l.append("Fizz")
            elif ni%5==0:
                l.append("Buzz")
            else:
                l.append(str(ni))
        return l
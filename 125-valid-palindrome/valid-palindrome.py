class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=""
        for i in s.lower():
            if(i.isalnum()):
                n=n+i
        if (n==n[::-1]):
            return True

        else:
            return False


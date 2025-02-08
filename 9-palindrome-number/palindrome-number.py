class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        temp=x[::-1]
        if temp==x:
            return True
        else:
            return False
        
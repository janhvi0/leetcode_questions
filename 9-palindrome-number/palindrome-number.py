class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False  # Negative numbers are not palindromes
    
        original = x
        reversed_num = 0
        
        while x > 0:
            digit = x % 10  # Extract last digit
            reversed_num = reversed_num * 10 + digit  # Build reversed number
            x //= 10  # Remove last digit from x
        
        return original == reversed_num



        
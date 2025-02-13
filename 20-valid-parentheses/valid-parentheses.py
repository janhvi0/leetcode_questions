class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}  # Mapping of closing -> opening brackets

        for char in s:
            if char in bracket_map:  # If it's a closing bracket
                top_element = stack.pop() if stack else '#'  
                if top_element != bracket_map[char]:  # Check for matching pair
                        return False
            else:
                stack.append(char)  # Push opening brackets onto the stack

        return not stack  # Stack should be empty if valid
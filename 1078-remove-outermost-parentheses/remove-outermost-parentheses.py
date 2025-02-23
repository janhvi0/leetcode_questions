class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        result=[]
        for i in s:
            if i == '(':
                if stack:
                    result.append(i)
                stack.append(i)

            else:
                stack.pop()
                if stack:
                    result.append(i)

        return ''.join(result)    


            
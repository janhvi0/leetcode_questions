class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):  # Loop through each character in the first string
            char = strs[0][i]
            for s in strs[1:]:  # Compare with remaining strings
                if i >= len(s) or s[i] != char:  # Check if out of range or mismatch
                    return strs[0][:i]
    
        return strs[0]  # Entire first string is the prefix
                


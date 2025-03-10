class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        #dict or hashmap
        char_count = {}

        #saving the count of the charectors
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for char in t:
            if char in char_count:
                char_count[char] -=1

                if char_count[char] == 0:
                    del char_count[char]

            else:
                return False

        return len(char_count) == 0


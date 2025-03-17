class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split() # splitting the words string into seperate list
        if len(pattern) != len(words): #we're checking if the len of pattern is not equal to len of words ie 4: 5.
            return False # so, we return false
        d = {} # creating a empty dictionary to store the char and word in the form of key value pair
        seen = set() # creating a set to store all the seen words so that we that word is mapped to other char
        for i, char in enumerate(pattern): # for every i and char in pattern looping together
            if char not in d: # if the current char is not in d dictionary
                if words[i] in seen: # if the current word is in seen that means it's mapped to some other char
                    return False # so, we return false
                d[char] = words[i] #if not, we mapped d of char to the current word
                seen.add(words[i]) # and add that word to our seen set
            else:
                if d[char] != words[i]: #if d of char is not equal to words of i 
                    return False # we return false
        return True # returning true as we passed all the cases
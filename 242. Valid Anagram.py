#Solution 1: Using count method with strings.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_ana = False
        if(len(s) != len(t)):
            return False
        for letter in s:
            if(s.count(letter) == t.count(letter)):
                is_ana = True
            else:
                is_ana = False
                break
        return is_ana


#Solution 2 using a hashmap.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}
        for c in s:
            if c in anagram:
                anagram[c] +=1
            else:
                anagram[c] =1
        for c in t:
            if c in anagram:
                anagram[c] -=1
            else:
                return False
        is_anagram = False
        for value in anagram.values():
            if(value == 0):
                is_anagram = True
            else:
                is_anagram = False
                break
        return is_anagram

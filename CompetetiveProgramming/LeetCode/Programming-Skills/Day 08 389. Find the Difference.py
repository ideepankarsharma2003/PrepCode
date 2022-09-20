class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if i not in s:
                return i 
            else:
                s= s.replace(i, '', 1)
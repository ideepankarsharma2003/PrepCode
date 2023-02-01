# https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1164/

class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.split()
        slist.reverse()
        return ' '.join(slist)

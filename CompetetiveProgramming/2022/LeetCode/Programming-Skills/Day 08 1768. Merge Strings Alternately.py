class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1= len(word1)
        l2= len(word2)
        
        l= ''
        if l1>l2:
            i=0
            while i<l2:
                l+=word1[i]
                l+=word2[i]
                i+=1
            l+=word1[i:]
        elif l2>l1:
            i=0
            while i<l1:
                l+=word1[i]
                l+=word2[i]
                i+=1
            l+=word2[i:]
        else:
            i=0
            while i<l1:
                l+=word1[i]
                l+=word2[i]
                i+=1
        
        return l
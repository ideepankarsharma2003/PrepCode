class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.split()
        for i in range(len(slist)):
            slist[i] = ''.join(reversed(slist[i]))
        # print(slist)
        return ' '.join(slist)

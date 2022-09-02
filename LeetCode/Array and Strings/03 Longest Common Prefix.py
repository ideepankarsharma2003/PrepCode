# https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1162/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        l = len(strs[0])
        for i in range(l):
            x = strs[0][:i+1]
            # print(x)
            for s in strs:
                if s[:i+1] != x:
                    return ans
                    # break
            ans = x
        return ans

class Solution:
    def freqAlphabets(self, s: str) -> str:

        d = {}
        for i in range(97, 97+26):
            # print(chr(i))
            if i < 106:
                d[str(i-96)] = chr(i)
            else:
                d[str(i-96) + '#'] = chr(i)
        ans = ''
        i = 0
        l = len(s)
        while(i < l):
            if i+2 < l and s[i+2] == '#':
                ans += d[s[i:i+3]]
                i += 3
            else:
                ans += d[s[i]]
                i += 1
        return ans

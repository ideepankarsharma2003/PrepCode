class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for i in ransomNote:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1

        print(d)
        for i in magazine:
            if i in d.keys():
                if d[i] != 0:
                    #     return False
                    # else:
                    d[i] -= 1

        l = list(d.values())
        if max(l) != 0:
            return False
        return True

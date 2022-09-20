class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        st1 = set()
        st2 = set()
        l = len(s1)
        for i in range(l):
            if s1[i] != s2[i]:
                count += 1
                st1.add(s1[i])
                st2.add(s2[i])

        if count == 0 or count == 2:
            if st1 == st2:
                return True
        else:
            return False

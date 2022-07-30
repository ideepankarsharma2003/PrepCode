class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ai = int(a, 2)
        bi = int(b, 2)
        # print(ai, bi)
        si = ai+bi
        s = bin(si)
        return s[2:]

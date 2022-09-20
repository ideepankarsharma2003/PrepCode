class Solution:
    def hammingWeight(self, n: int) -> int:
        s = bin(n)
        return s.count('1')

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        l = [int(i) for i in s]
        s = sum(l)
        p = 1
        for i in l:
            p *= i
        return p-s

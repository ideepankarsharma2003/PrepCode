def signFunc(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        mul = 1
        for i in nums:
            mul *= i
        return signFunc(mul)

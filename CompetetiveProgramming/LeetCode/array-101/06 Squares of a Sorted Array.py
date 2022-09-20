class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = [i**2 for i in nums]
        l.sort()
        return l

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        dum = nums.copy()
        dum.sort()
        if dum[-1] >= 2*dum[-2]:
            return nums.index(dum[-1])
        else:
            return -1

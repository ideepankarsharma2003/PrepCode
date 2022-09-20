class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        l = [str(i) for i in nums]

        count = 0
        for i in l:
            if len(i) % 2 == 0:
                count += 1
        return count

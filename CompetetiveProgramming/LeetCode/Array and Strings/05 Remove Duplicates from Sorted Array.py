class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        d = {}
        for i in nums:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1

        for i in d.keys():
            while d[i] > 1:
                nums.remove(i)
                d[i] -= 1

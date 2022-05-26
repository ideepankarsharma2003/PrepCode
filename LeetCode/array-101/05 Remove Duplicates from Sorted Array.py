class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        l = list(d.keys())
        for i in l:
            while d[i] > 1:
                nums.remove(i)
                d[i] -= 1

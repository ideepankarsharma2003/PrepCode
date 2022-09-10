class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > len(nums):
            k = k-len(nums)
        l = nums[:-k]
        for i in l:
            nums.remove(i)
            nums.append(i)

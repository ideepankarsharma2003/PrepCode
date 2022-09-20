class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in range(len(nums)):
            if nums[j]==0:
                nums.pop(j)
                nums.append(0)
            else:
                j+=1
        
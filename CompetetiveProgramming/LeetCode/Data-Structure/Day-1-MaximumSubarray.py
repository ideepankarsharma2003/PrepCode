class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = nums[0]

        recent_sum = 0
        for num in nums:
            recent_sum += num

            if recent_sum > max_sum:
                max_sum = recent_sum

            if recent_sum < 0:
                recent_sum = 0

        return max_sum

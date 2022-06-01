class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        x = 0
        m = 0
        l = len(nums)
        for i in range(l-2):
            l2 = nums[i: i+3]
            if l2[1]+l2[2] <= l2[0] or l2[0]+l2[1] <= l2[2] or l2[0]+l2[2] <= l2[1]:
                m = 0
            else:
                x = sum(l2)
            m = max(m, x)

        return m

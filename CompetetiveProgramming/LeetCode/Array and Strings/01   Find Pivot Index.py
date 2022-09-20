class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l= len(nums)
        ls= 0
        rs= sum(nums)
        for i in range(l):
            x= nums[i]
            rs-=x
            if ls==rs:
                return i
            ls+=x
        return -1
            
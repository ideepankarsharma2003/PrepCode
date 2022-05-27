class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # r=[]
        # l= len(nums)
        # for i in range(1, l+1):
        #     if i not in nums:
        #         r.append(i)
        # return r
        return set(range(1, len(nums) + 1)) - set(nums)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # l={}
        # for i in nums:
        #     if i in l.keys():
        #         return True
        #     else:
        #         l[i]=1

        if len(nums) != len(set(nums)):
            return True
        # x= []
        # l= len(nums)
        # for i in range(l):
        #     m= nums.pop()
        #     if m in x:
        #         return True
        #     else:
        #         x.append(m)
        return False

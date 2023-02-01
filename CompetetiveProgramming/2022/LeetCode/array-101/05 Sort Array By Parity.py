class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        j = 0
        for i in range(len(nums)):
            if nums[j] % 2 == 0:
                x = nums.pop(j)
                nums.insert(0, x)
                j += 1
            else:
                x = nums.pop(j)
                nums.append(x)
                # j+=1
        return nums

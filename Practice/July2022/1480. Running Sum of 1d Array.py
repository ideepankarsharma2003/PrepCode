class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        dum = []
        dum.append(nums[0])
        for i in range(1, len(nums)):
            dum.append(sum(nums[:i+1]))
        print(dum)
        return (dum)

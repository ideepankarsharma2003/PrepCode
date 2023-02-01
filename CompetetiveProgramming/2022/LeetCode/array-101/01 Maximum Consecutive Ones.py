class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = []
        count = 0
        for i in nums:
            if i == 1:
                # print(f'i= {i}')
                count += 1
            else:
                # print(f'count= {count}')
                l.append(count)
                count = 0
        l.append(count)
        # print(l)
        return max(l)

        
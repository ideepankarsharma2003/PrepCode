class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = []
        mxS = []
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            elif i == 0:
                l.append(count)
                count = 0
        l.append(count)

        # print(f'l = {l}')
        if len(l) == 1:
            return l[0]
        # prev= l[0]
        for i in range(len(l)-1):
            mxS.append(l[i]+l[i+1])

        # print(f'mxS = {mxS}')

        return max(mxS)+1

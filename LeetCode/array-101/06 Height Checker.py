class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        expected= heights.copy()
        expected.sort()
        for i in range(len(heights)):
            if heights[i]!=expected[i]:
                count+=1
        return count
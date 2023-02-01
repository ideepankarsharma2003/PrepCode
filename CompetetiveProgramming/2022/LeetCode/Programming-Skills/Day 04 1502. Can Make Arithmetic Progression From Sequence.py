class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        l = len(arr)
        x = arr[1] - arr[0]
        for i in range(2, l):
            if arr[i] - arr[i-1] != x:
                return False
        return True

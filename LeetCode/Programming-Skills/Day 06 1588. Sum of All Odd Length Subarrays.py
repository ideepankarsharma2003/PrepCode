class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        k = 1
        l = len(arr)
        if l % 2 != 0:
            s += sum(arr)

        while k < l:
            for i in range(0, l-k+1):
                s += sum(arr[i:i+k])
                print(f'arr= {(arr[i:i+k])}')
            k += 2

        return s

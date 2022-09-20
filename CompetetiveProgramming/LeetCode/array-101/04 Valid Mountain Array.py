class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        inc = 0
        if len(arr) < 3:
            return False
        idx = 0
        for i in range(1, len(arr)-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                inc += 1
                idx = i
            # elif arr[i] >= arr[i-1]:
            #     inc += 1
            #     # idx=i

        if inc == 1:
            prev = arr[0]
            for i in arr[1:idx+1]:
                if i <= prev:
                    return False
                prev = i

            for i in arr[idx+1:]:
                if i >= prev:
                    return False
                prev = i

            return True
        return False

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[j] == 2*arr[i] and i != j:
                    # print(i, j)
                    return True

            # print()

        return False

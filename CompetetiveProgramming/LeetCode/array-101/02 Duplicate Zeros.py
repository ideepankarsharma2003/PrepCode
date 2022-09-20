class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
#         count= arr.count(0)
#         l= len(arr)
#         i=0
#         while i<l:
#             if arr[i]==0:
#                 arr.insert(i+1, 0)
#                 i+=2
#             else:
#                 i+=1
# #         arr= arr[:l]
        count = arr.count(0)
        l = len(arr)
        i = 0
        # print(f'l= {l}')
        while i < l:
            # print(i)
            if arr[i] == 0:
                arr.insert(i+1, 0)
                i += 2
            else:
                i += 1
        # arr= arr[:l]
        i = len(arr)
        # print(f'i= {i}')
        while i > l:
            arr.pop()
            i -= 1
        # print(arr)

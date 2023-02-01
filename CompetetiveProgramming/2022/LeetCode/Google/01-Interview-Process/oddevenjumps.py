# def oddjump(arr, jumpIndex, jump):
#     i=jumpIndex
#     newArr= arr[i+1:].sort()
#     smallValue= newArr[0]
#     j= arr.index(smallValue)
#     if arr[i]<=smallValue:
#         if j>i:
#             jump+=1
#             jumpIndex=j
#     # for j in range(i+1, len(arr)-1):
#     #     if arr[i]<=arr[j]:
#     #         jump+=1
#     #         jumpIndex=j
#     #         break
#     return (jumpIndex, jump)

# def evenjump(arr, jumpIndex, jump):
#     i = jumpIndex
#     newArr = arr[i+1:].sort()
#     largeValue = newArr[-1]
#     j = arr.index(largeValue)
#     if arr[i] >= largeValue:
#         if j > i:
#             jump += 1
#             jumpIndex = j

#     # for j in range(i+1, len(arr)-1):
#     #     if arr[i] >= arr[j]:
#     #         jump += 1
#     #         jumpIndex = j
#     #         break
#     return (jumpIndex, jump)

class Solution(object):
    def oddEvenJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        goodInd= 0
        indices = len(arr)

        for cIndex in range(indices):
            jump=0
            jumpInd=cIndex
            for i in range(cIndex, indices):
                if jump%2==0:
                    # jumpInd, jump= evenjump(arr[i:], jumpInd, jump)
                    newArr = arr[i+1:]
                    newArr= newArr.sort()
                    largeValue = newArr[-1]
                    j = arr.index(largeValue)
                    if arr[i] >= largeValue:
                        if j > i:
                            jump += 1
                            jumpIndex = j
                else: # odd number jumps
                    # jumpInd, jump= oddjump(arr[i:], jumpInd, jump)
                    newArr= arr[i+1:].sort()
                    smallValue= newArr[0]
                    j= arr.index(smallValue)
                    if arr[i]<=smallValue:
                        if j>i:
                            jump+=1
                            jumpInd=j
            if jumpInd==(indices-1):
                goodInd+=1
            
        return goodInd


arr = [10, 13, 12, 14, 15]
obj= Solution()
print((obj.oddEvenJumps(arr)))

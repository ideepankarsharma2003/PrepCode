class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l= len(arr)
        l-=1
        for i in range(l):
            mX= max(arr[i+1:])
            arr.pop(i)
            arr.insert(i, mX)
        arr.pop()
        arr.append(-1)
        return arr
        
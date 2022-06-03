class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = len(nums1)
        ans = []
        for i in range(l1):
            j = nums2.index(nums1[i])

            for k in (nums2[j:]):
                if k > nums2[j]:
                    ans.append(k)
                    break
            else:
                ans.append(-1)
        return ans

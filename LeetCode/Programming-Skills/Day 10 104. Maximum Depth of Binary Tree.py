# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# rDepth= 0
# lDepth= 0


class Solution:
    rDepth = 0
    lDepth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

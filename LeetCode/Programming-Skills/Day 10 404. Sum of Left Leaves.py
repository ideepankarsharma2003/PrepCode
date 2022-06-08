# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def leftLeaves(root, isLeft):
    if not root:
        return 0

    if not root.left and not root.right and isLeft:
        return root.val
    else:
        return leftLeaves(root.left, True) + leftLeaves(root.right, False)


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return leftLeaves(root.left, True) + leftLeaves(root.right, False)

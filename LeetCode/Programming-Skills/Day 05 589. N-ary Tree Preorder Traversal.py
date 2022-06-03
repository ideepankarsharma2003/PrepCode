
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack = []

        # code for DFS
        def DFS(root):
            if not root:
                return
            else:
                for i in root.children:
                    stack.append(i.val)
                    DFS(i)

        if not root:
            return
        stack.append(root.val)
        DFS(root)
        return stack

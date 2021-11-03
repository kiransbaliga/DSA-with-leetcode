# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traversal(root,i):
            if root:
                if root.left == None and root.right == None:
                    return i*10+root.val
                else:
                    return traversal(root.left,i*10+root.val)+traversal(root.right,i*10+root.val)
            else:
                return 0
        if root:
            return traversal(root,0)
        else:
            return 0
        
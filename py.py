# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def formtree(start,end): 
            if start==end: return None   # to check if the tree is empty
            res=[]                       
            for i in range(start,end):      # loop each number 
                for l in formtree(start,i) or [None]:  # form to the left of the tree i.e. for numbers less than the selected number
                    for r in formtree(i+1,end) or [None]: # form to the right of the tree i.e. for numbers greater than the selected number
                        node= TreeNode(i)   # create a node
                        node.left=l     
                        node.right=r
                        res.append(node)
            return res
        return formtree(1,n+1)
        
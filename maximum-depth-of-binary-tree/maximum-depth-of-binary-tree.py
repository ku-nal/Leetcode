# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        
        def depth(root):
            if root==None:
                return 0
            left=depth(root.left)
            right=depth(root.right)
            
            return max(left,right)+1
        self.ma=depth(root)
        return self.ma
    
            

        
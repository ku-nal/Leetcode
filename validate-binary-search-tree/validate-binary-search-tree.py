# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isbst(root,float('-inf'),float('inf'))
    
    def isbst(self,tree,minv,maxv):
        if tree is None:
            return True
        if tree.val <= minv or tree.val >= maxv:
            return False
        leftsub=self.isbst(tree.left,minv,tree.val)
        return leftsub and self.isbst(tree.right,tree.val,maxv)
    
        
        
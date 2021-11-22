# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        def recur(root,val):
            if root==None:
                return None
            if val==root.val:
                return root
            elif val<root.val:
                return recur(root.left,val)
            else:
                return recur(root.right,val)
        return recur(root,val)
            
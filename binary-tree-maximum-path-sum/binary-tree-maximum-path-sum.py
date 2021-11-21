# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=float('-inf')
        def helper(root):
            if root==None:
                return 0
            left=helper(root.left)
            right=helper(root.right)
            
            self.ans=max(right+left+root.val,self.ans)
            
            return max(left+root.val,right+root.val,0)
        helper(root)
        return self.ans
        
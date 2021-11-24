# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype:
        """
        self.c=0
        def recur(root):
            if root==None:
                return
            left=recur(root.left)
            if left:return True
            self.c+=1
            if self.c==k:
                self.ans=root.val
                return True
            
            right=recur(root.right)
            if right:return True
        recur(root)
        return self.ans
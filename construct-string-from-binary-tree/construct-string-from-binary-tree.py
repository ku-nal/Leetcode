# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if root.left==None and root.right==None:return str(root.val)
        self.st=""
        def helper(root):
            if root==None:
                self.st+=")"
                return
            elif root.left==None and root.right==None:
                self.st+=str(root.val)+")"
                return
            self.st+=str(root.val)+"("
            helper(root.left)
            if root.right!=None:
                self.st+="("
                helper(root.right)
            self.st+=")"
        helper(root)
        i=0
        return self.st[:-1]
            
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.ans=""
        
        def recur(root):
            if root==None:
                self.ans+="N"
                return
            self.ans+=str(root.val)
            recur(root.left)
            recur(root.right)
        
        recur(root)
        self.ans1=self.ans
        self.ans=""
        def recur1(root):
            if root==None:
                self.ans+="N"
                return
            self.ans+=str(root.val)
            recur1(root.right)
            recur1(root.left)
        recur1(root)
        print(self.ans1,self.ans)
        if self.ans==self.ans1:return True
        return False
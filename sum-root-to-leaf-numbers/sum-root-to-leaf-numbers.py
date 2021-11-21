# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.li=[]
        def recur(root,path):
            if root==None:
                return
            if root.right==None and root.left==None:
                self.li.append(path+str(root.val))
            
            recur(root.left,path+str(root.val))
            recur(root.right,path+str(root.val))
        recur(root,"")
        
        ans=0
        for i in self.li:
            ans+=int(i)
        return ans
        
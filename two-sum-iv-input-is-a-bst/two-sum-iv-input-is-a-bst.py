# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.li=[]
        def recur(root):
            if root==None:
                return
            recur(root.left)
            self.li.append(root.val)
            recur(root.right)
        recur(root)
        i,j=0,len(self.li)-1
        
        while i!=j:
            if self.li[i]+self.li[j]==k:
                return True
            elif self.li[i]+self.li[j]>k:
                j-=1
            else:
                i+=1
        return False
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    ans=[]
    def paths(self,root,s,ans):
        if root==None:
            return
        if not root.left and not root.right:
            ans.append(s+str(root.val))
            return
        self.paths(root.left,s+str(root.val)+"->",ans)
        self.paths(root.right,s+str(root.val)+"->",ans)
        
            
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root==None:
            return None
        if not root.left and not root.right:
            return [""+str(root.val)]
        ans=[]
        s=""
        self.paths(root,s,ans)
        return ans
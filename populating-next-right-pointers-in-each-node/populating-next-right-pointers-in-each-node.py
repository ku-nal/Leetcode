"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.li=[]
        
        def recur(root,lvl):
            if root==None:
                return
            if len(self.li)==lvl:
                self.li.append([root])
            else:
                self.li[lvl].append(root)
            recur(root.left,lvl+1)
            recur(root.right,lvl+1)
        
        recur(root,0)
        
        for i in range(len(self.li)):
            for j in range(len(self.li[i])):
                if j!=len(self.li[i])-1:
                    self.li[i][j].next=self.li[i][j+1]
                else:
                    self.li[i][j].next=None
        return root
                    
            
                
        
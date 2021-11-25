"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        self.visited={}
        def helper(root):
            if root==None:
                return 
            node=Node(root.val)
            self.visited[root.val]=node
            
            for neigh in root.neighbors:
                if neigh.val not in self.visited:
                    node.neighbors.append(helper(neigh))
                else:
                    node.neighbors.append(self.visited[neigh.val])
            
            return node
        
        return helper(node)
        
        
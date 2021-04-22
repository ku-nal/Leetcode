class Solution(object):
    def findMaximumXOR(self, li):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(li)
        class node():
            def __init__(self):
                self.left=None
                self.right=None
        
        head=node()
        for i in range(n):
            curr=head
            for j in reversed(range(32)):
                val=(li[i]>>j)&1
                
                if val==1:
                    if curr.right==None:
                        curr.right=node()
                    curr=curr.right
                else:
                    if curr.left==None:
                        curr.left=node()
                    curr=curr.left
                    
        ans=float('-inf')
        for i in range(n):
            curr=head
            temp=0
            for j in reversed(range(32)):
                val=(li[i]>>j)&1
                
                if val==1:
                    if curr.left is not None:
                        temp+=2**j
                        curr=curr.left
                    else:
                        curr=curr.right
                else:
                    if curr.right is not None:
                        temp+=2**j
                        curr=curr.right
                    else:
                        curr=curr.left
            ans=max(ans,temp)
        
        return ans
            
        
        
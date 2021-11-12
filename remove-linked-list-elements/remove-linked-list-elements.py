# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ans=ListNode()
        ans.next=head
        ptr=ans
        while ptr and ptr.next!=None:
            if ptr.next.val==val:
                ptr.next=ptr.next.next
            else:
                ptr=ptr.next
        return ans.next
            
        
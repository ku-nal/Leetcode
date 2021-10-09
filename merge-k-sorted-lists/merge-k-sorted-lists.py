# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        li=[]
        for i in range(len(lists)):
            if lists[i]!=None:
                li.append(lists[i])
        if len(li)==0:
            return None
        
        pos=0
        mi=float('inf')
        ans=ListNode()
        temp=ans
        while len(li)>0:
            for i in range(len(li)):
                if mi>li[i].val:
                    pos=i
                    mi=li[i].val
            
            
            li[pos]=li[pos].next
            if li[pos]==None or li[pos].val==None:
                li.pop(pos)
            temp.val=mi
            if len(li)>0:
                temp.next=ListNode()
                temp=temp.next
            mi=float('inf')

        return ans
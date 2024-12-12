# 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length=0
        top=head
        while top!=None:
            length+=1
            top=top.next
        # print(length)
        
        index=(length-n)
        return self.remove(head,index)

    def remove(self,head,index):
        l=0
        top=head
        # print(index)
        if(index==0):
            return top.next
        for i in range(index-1):
            l+=1
            top=top.next
        top.next = top.next.next

        return head
# 82. Remove Duplicates from Sorted List II

# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        domey=ListNode(0)
        domey.next=head

        prev=domey
        current=head

        while current:
            while (current.next and current.val==current.next.val):
                current=current.next          

            if(prev.next==current):
                prev=prev.next
            else:
                prev.next=current.next
            
            current=current.next
        return domey.next
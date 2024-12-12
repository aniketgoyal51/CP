# 24. Swap Nodes in Pairs

# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        domey=ListNode(0)
        domey.next=head
        current =domey

        while current.next and current.next.next:
            first=current.next
            second=current.next.next
        
            first.next=second.next
            second.next=first
            current.next=second
            

            current=first
        return domey.next
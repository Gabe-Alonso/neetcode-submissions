# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:
            n = head.next
            p = None
            done = False
            while head is not None:
                #print(head.val)
                #print(head.next)
                head.next = p
                p = head
                head = n
                if head is not None:
                    n = head.next
                #print(head)
            return p
        else:
            return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        if not head:
            return None
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        for _ in range(n - 1):
            stack.pop()
        if stack:
            kill = stack.pop()
            if stack:
                stack[-1].next = kill.next
            else:
                head = kill.next
        return head
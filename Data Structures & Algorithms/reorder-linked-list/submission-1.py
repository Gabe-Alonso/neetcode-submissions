# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = 0
        cur = head
        stack = []
        while cur:
            stack.append(cur)
            l += 1
            cur = cur.next
        cur = head
        for s in stack:
            print(s.val)
        while l > 0:
            print(cur.val)
            curNext = cur.next
            l -= 1
            if l > 0:
                cur.next = stack.pop()
                cur = cur.next
                print(cur.val)
                l -= 1
                cur.next = curNext
                cur = cur.next
        cur.next = None
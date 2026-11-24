"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ht = {None: None}
        cur1 = head
        while cur1:
            cur2 = Node(cur1.val)
            ht[cur1] = cur2
            cur1 = cur1.next
        cur1 = head
        while cur1:
            cur2 = ht[cur1]
            cur2.next = ht[cur1.next]
            cur2.random = ht[cur1.random]
            cur1 = cur1.next
        return ht[head]
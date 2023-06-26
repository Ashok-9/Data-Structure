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
        if head is None:
            return None
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = curr.next.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next


        dummy = Node(0)
        curr = head
        new_head = curr.next
        new_curr = new_head

        while curr:
            curr.next = curr.next.next
            curr = curr.next
            if new_curr.next:
                new_curr.next = new_curr.next.next
                new_curr = new_curr.next

        return new_head
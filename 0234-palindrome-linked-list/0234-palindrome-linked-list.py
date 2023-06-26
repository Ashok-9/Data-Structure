# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next==None:
            return True

        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        mid=slow
        prev = None
        current = mid

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        root=head
        
        # while root!=mid:
        #     print(root.val)
        #     root=root.next
        # while prev:
        #     print(prev.val)
        #     prev=prev.next
        while root!=mid and prev:
            if root.val==prev.val:
                root=root.next
                prev=prev.next
            else:
                return False
        else: 
            return True
        

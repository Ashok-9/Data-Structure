# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        c=0
        while curr:
            curr=curr.next
            c+=1

        s=c-n
        print(c,s)
        c1=1
        curr=head
        if s==0:
            head=head.next
            return head
        while c1!=s:
            curr=curr.next
            c1+=1
        curr.next=curr.next.next
        return head


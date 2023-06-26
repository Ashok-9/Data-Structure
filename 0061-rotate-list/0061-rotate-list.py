# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None :
            return head
        cur=head
        c=0
        while cur.next:
            c+=1
            cur=cur.next
        c+=1
        cur.next=head
        k=k%c
        
        d=c-k
        print(d,c,k)
        cur=head
        c=1
        while c!=d:
            c+=1
            cur=cur.next
           
        head=cur.next
        cur.next=None
        return head
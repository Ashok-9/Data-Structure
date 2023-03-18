# Definition for singly-linked list.
p=None
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        global p
        p=head
        temp1=None
        while p:
            temp=p.next
            p.next=temp1
            temp1=p
            p=temp
        head.self=None
        

    def display(self,head):
        start=head
        while start:
            print(start.val)
            start=start.next
        
arr = [1,2,3,4,5]
head=ListNode(arr[0])
h=head
for i in range(1,len(arr)):
    h.next=ListNode(arr[i])
    h=h.next
s=Solution()

s.reverseList(head)
s.display(p)


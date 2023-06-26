# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a=headA
        b=headB
        flag=0
        flag1=0
        while a!=b:
            if a==None:
                if flag==1:
                    return None
                a=headB
                flag=1
            else:
                
                a=a.next
            if b==None:
                if flag1==1:
                    return None
                flag1=1
                b=headA
            else:
                
                b=b.next
        return a
     
        # flag=0
        # flag1=0
        # while a or b :
        #     if a==b:
        #         return True
        #     if a==None:
        #         if flag==1:
        #             break
        #         a=headB
        #         flag=1
                
        #     else:    
        #         a=a.next
        #     if b==None :
        #         if flag==1:
        #             break
        #         b=headA
        #         flag1=1
        #     else:
        #         b=b.next
        # return False
        
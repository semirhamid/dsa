# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        result = answer = ListNode(None)
        while l1 and l2:
            sm = rem + l1.val + l2.val
            if(sm > 9):
                result.next = ListNode(sm -10)
                rem = 1
            else:
                rem = 0
                result.next = ListNode(sm)
            l1 = l1.next
            l2 = l2.next
            result = result.next
        
        while l1:
            sm = rem + l1.val
            if(sm > 9):
                result.next = ListNode(sm -10)
                rem = 1
            else:
                rem = 0
                result.next = ListNode(sm)
            l1 = l1.next
            result = result.next
        
        while l2:
            sm = rem + l2.val
            if(sm > 9):
                result.next = ListNode(sm -10)
                rem = 1
            else:
                rem = 0
                result.next = ListNode(sm)
            l2 = l2.next
            result = result.next
        if rem != 0:
            result.next = ListNode(rem)
        
        return answer.next

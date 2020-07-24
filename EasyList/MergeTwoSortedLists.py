class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        dummy = ListNode(-1)
        newList = dummy 
        while (l1 != None and l2 != None):
            if(l1.val <= l2.val):
                newList.next = l1
                l1 = l1.next
            else:
                newList.next = l2
                l2 = l2.next
            newList = newList.next
        newList.next = l1 if l1 else l2
        return dummy.next
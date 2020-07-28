# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None: return False
        iter1 = head
        iter2 = head
        while iter1 and iter2 and iter1.next != None:
            iter1 = iter1.next.next
            iter2 = iter2.next
            if(iter1 == iter2):
                return True
        return False 
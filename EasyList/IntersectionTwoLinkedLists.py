class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA and not headB: 
            return None
        runnerA = headA
        runnerB = headB

        while runnerA != runnerB:
            if runnerA == None:
                runnerA = headB
            else:
                runnerA = runnerA.next
            if runnerB == None:
                runnerB = headA
            else:
                runnerB = runnerB.next
        return runnerA

        